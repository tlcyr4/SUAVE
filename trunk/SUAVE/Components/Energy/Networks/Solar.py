# Solar.py
# 
# Created:  Jun 2014, E. Botero
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE

# package imports
import numpy as np
from SUAVE.Components.Propulsors.Propulsor import Propulsor

from SUAVE.Core import Data

# ----------------------------------------------------------------------
#  Network
# ----------------------------------------------------------------------
class Solar(Propulsor):
    """ SUAVE.Components.Energy.Networks.Solar()
        Solar-powered propeller
    """
    def __defaults__(self): 
        self.solar_flux        = None
        self.solar_panel       = None
        self.motor             = None
        self.propeller         = None
        self.esc               = None
        self.avionics          = None
        self.payload           = None
        self.solar_logic       = None
        self.battery           = None
        self.nacelle_diameter  = None
        self.engine_length     = None
        self.number_of_engines = None
        self.tag               = 'network'
    
    # manage process with a driver function
    def evaluate_thrust(self,state):
        """ SUAVE.Components.Energy.Networks.Solar.evaluate_thrust(state)
            Function called when propulsor is called by Energy Analysis, evaluates thrust of propulsor

            Passes state.conditions Through components and uses self.thrust to compute thrust.
            See component documentation and Thrust documentation for more details.

            IMPORTANT: For more details, see component documentations


        """
        # unpack
        conditions  = state.conditions
        numerics    = state.numerics
        solar_flux  = self.solar_flux
        solar_panel = self.solar_panel
        motor       = self.motor
        propeller   = self.propeller
        esc         = self.esc
        avionics    = self.avionics
        payload     = self.payload
        solar_logic = self.solar_logic
        battery     = self.battery
       
        # Set battery energy
        battery.current_energy = conditions.propulsion.battery_energy
        
        # step 1
        solar_flux.solar_radiation(conditions)
        # link
        solar_panel.inputs.flux = solar_flux.outputs.flux
        # step 2
        solar_panel.power()
        # link
        solar_logic.inputs.powerin = solar_panel.outputs.power
        # step 3
        solar_logic.voltage()
        # link
        esc.inputs.voltagein =  solar_logic.outputs.system_voltage
        # Step 4
        esc.voltageout(conditions)
        # link
        motor.inputs.voltage = esc.outputs.voltageout 
        # step 5
        motor.omega(conditions)
        # link
        propeller.inputs.omega =  motor.outputs.omega
        # step 6
        F, Q, P, Cplast = propeller.spin(conditions)
     
        # Check to see if magic thrust is needed, the ESC caps throttle at 1.1 already
        eta = conditions.propulsion.throttle[:,0,None]
        P[eta>1.0] = P[eta>1.0]*eta[eta>1.0]
        F[eta>1.0] = F[eta>1.0]*eta[eta>1.0]
        
        # Run the avionics
        avionics.power()
        # link
        solar_logic.inputs.pavionics =  avionics.outputs.power
        
        # Run the payload
        payload.power()
        # link
        solar_logic.inputs.ppayload = payload.outputs.power
        
        # Run the motor for current
        motor.current(conditions)
        # link
        esc.inputs.currentout =  motor.outputs.current
        
        # Run the esc
        esc.currentin()
        # link
        solar_logic.inputs.currentesc  = esc.outputs.currentin*self.number_of_engines
        solar_logic.inputs.volts_motor = esc.outputs.voltageout 
        #
        solar_logic.logic(conditions,numerics)
        # link
        battery.inputs = solar_logic.outputs
        battery.energy_calc(numerics)
        
        #Pack the conditions for outputs
        rpm                                  = motor.outputs.omega*60./(2.*np.pi)
        current                              = solar_logic.inputs.currentesc
        battery_draw                         = battery.inputs.power_in 
        battery_energy                       = battery.current_energy
        
        conditions.propulsion.solar_flux       = solar_flux.outputs.flux  
        conditions.propulsion.rpm              = rpm
        conditions.propulsion.current          = current
        conditions.propulsion.battery_draw     = battery_draw
        conditions.propulsion.battery_energy   = battery_energy
        conditions.propulsion.motor_torque     = motor.outputs.torque
        conditions.propulsion.propeller_torque = Q        
        
        #Create the outputs
        F    = self.number_of_engines * F * [1,0,0]      
        mdot = np.zeros_like(F)

        results = Data()
        results.thrust_force_vector = F
        results.vehicle_mass_rate   = mdot

        return results
    
    
    def unpack_unknowns(self,segment,state):
        """
            Here we are going to unpack the unknowns (Cp) provided for this network
        """
        
        #
        state.conditions.propulsion.propeller_power_coefficient = state.unknowns.propeller_power_coefficient

        return
    
    def residuals(self,segment,state):
        """
            Here we are going to pack the residuals from the network
        """
        
        #
        
        # Unpack
        q_motor   = state.conditions.propulsion.motor_torque
        q_prop    = state.conditions.propulsion.propeller_torque
        
        # Return the residuals
        state.residuals.network[:,0] = q_motor[:,0] - q_prop[:,0]
        
        return        
            
    __call__ = evaluate_thrust