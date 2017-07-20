# Battery_Propeller.py
# 
# Created:  Jul 2015, E. Botero
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
class Battery_Propeller(Propulsor):
    """ SUAVE.Components.Energy.Networks.Battery_Propeller()
        A battery connected to a propeller
    """
    def __defaults__(self): 
        self.motor             = None
        self.propeller         = None
        self.esc               = None
        self.avionics          = None
        self.payload           = None
        self.battery           = None
        self.nacelle_diameter  = None
        self.engine_length     = None
        self.number_of_engines = None
        self.voltage           = None
        self.thrust_angle      = 0.0
        self.tag               = 'network'
    
    # manage process with a driver function
    def evaluate_thrust(self,state):
        """ SUAVE.Components.Energy.Networks.Battery_Propeller.evaluate_thrust(state)
            Function called when propulsor is called by Energy Analysis, evaluates thrust of propulsor

            Inputs:
                state. - state of the system (See self.propulsor documentation)
                    conditions. (passed to components, see documentation)
                        propulsion.
                            throttle
                            rpm
                            current
                            battery_draw
                            battery_energy
                            voltage_open_circuit
                            voltage_under_load
                            motor_torque
                            propeller_torque
                    numerics (passed to battery.energy_calc)

            Outputs:
                results.
                    vehicle_mass_rate
                    See self.propulsor documentation

            Properties Used:
                motor
                propeller
                esc
                avionics
                payload
                battery
                number_of_engines
                thrust_angle
                voltage

            Updates:
                state.conditions.propulsion.
                    battery_draw
                    battery_energy
                See self.propulsor documentation

        """
        # unpack
        conditions = state.conditions
        numerics   = state.numerics
        motor      = self.motor
        propeller  = self.propeller
        esc        = self.esc
        avionics   = self.avionics
        payload    = self.payload
        battery    = self.battery
        
        # Set battery energy
        battery.current_energy = conditions.propulsion.battery_energy  

        # Step 1 battery power
        esc.inputs.voltagein = state.unknowns.battery_voltage_under_load
        # Step 2
        esc.voltageout(conditions)
        # link
        motor.inputs.voltage = esc.outputs.voltageout 
        # step 3
        motor.omega(conditions)
        # link
        propeller.inputs.omega =  motor.outputs.omega
        propeller.thrust_angle = self.thrust_angle
        # step 4
        F, Q, P, Cp = propeller.spin(conditions)
        
        # Check to see if magic thrust is needed, the ESC caps throttle at 1.1 already
        eta        = conditions.propulsion.throttle[:,0,None]
        P[eta>1.0] = P[eta>1.0]*eta[eta>1.0]
        F[eta>1.0] = F[eta>1.0]*eta[eta>1.0]

        # Run the avionics
        avionics.power()

        # Run the payload
        payload.power()
        
        # Run the motor for current
        motor.current(conditions)
        # link
        esc.inputs.currentout =  motor.outputs.current
        
        # Run the esc
        esc.currentin()

        # Calculate avionics and payload power
        avionics_payload_power = avionics.outputs.power + payload.outputs.power

        # Calculate avionics and payload current
        avionics_payload_current = avionics_payload_power/self.voltage

        # link
        battery.inputs.current  = esc.outputs.currentin*self.number_of_engines + avionics_payload_current
        battery.inputs.power_in = -(esc.outputs.voltageout*esc.outputs.currentin*self.number_of_engines + avionics_payload_power)
        battery.energy_calc(numerics)        
    
        # Pack the conditions for outputs
        rpm                  = motor.outputs.omega*60./(2.*np.pi)
        current              = esc.outputs.currentin
        battery_draw         = battery.inputs.power_in 
        battery_energy       = battery.current_energy
        voltage_open_circuit = battery.voltage_open_circuit
        voltage_under_load   = battery.voltage_under_load    
          
        conditions.propulsion.rpm                  = rpm
        conditions.propulsion.current              = current
        conditions.propulsion.battery_draw         = battery_draw
        conditions.propulsion.battery_energy       = battery_energy
        conditions.propulsion.voltage_open_circuit = voltage_open_circuit
        conditions.propulsion.voltage_under_load   = voltage_under_load  
        conditions.propulsion.motor_torque         = motor.outputs.torque
        conditions.propulsion.propeller_torque     = Q
        
        # Create the outputs
        F    = self.number_of_engines * F * [np.cos(self.thrust_angle),0,-np.sin(self.thrust_angle)]      
        mdot = np.zeros_like(F)

        results = Data()
        results.thrust_force_vector = F
        results.vehicle_mass_rate   = mdot
        
        
        return results
    
    
    def unpack_unknowns(self,segment,state):
        """ SUAVE.Components.Energy.Networks.Battery_Propeller.unpack_unknowns(segment,state)
            Here we are going to unpack the unknowns (Cp) provided for this network

            Inputs:
                segment - unused
                state.unknowns.
                    propeller_power_coefficient
                    battery_voltage_under_load

            Outputs:
                See Updates

            Updates:
                state.conditions.propulsion.
                    propeller_power_coefficient
                    battery_voltage_under_load
        """

        state.conditions.propulsion.propeller_power_coefficient = state.unknowns.propeller_power_coefficient
        state.conditions.propulsion.battery_voltage_under_load  = state.unknowns.battery_voltage_under_load
        
        return
    
    def residuals(self,segment,state):
        """ SUAVE.Components.Energy.Networks.Battery_Propeller.residuals(segment,state)
            Here we are going to pack the residuals (torque,voltage) from the network

            Inputs:
                segment - unused
                state.conditions.propulsion.
                    motor_torque
                    propeller_torque
                    voltage_under_load
                unknowns.battery_voltage_under_load

            Outputs:
                See Updates

            Properties Used:
                voltage

            Updates:
                state.residuals.network
        """
        
        #
        
        # Unpack
        q_motor   = state.conditions.propulsion.motor_torque
        q_prop    = state.conditions.propulsion.propeller_torque
        v_actual  = state.conditions.propulsion.voltage_under_load
        v_predict = state.unknowns.battery_voltage_under_load
        v_max     = self.voltage
        
        # Return the residuals
        state.residuals.network[:,0] = q_motor[:,0] - q_prop[:,0]
        state.residuals.network[:,1] = (v_predict[:,0] - v_actual[:,0])/v_max
        
        return    
            
    __call__ = evaluate_thrust
