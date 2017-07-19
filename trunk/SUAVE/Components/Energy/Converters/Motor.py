# Motor.py
#
# Created:  Jun 2014, E. Botero
# Modified: Jan 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE

# package imports
import numpy as np
from SUAVE.Components.Energy.Energy_Component import Energy_Component

# ----------------------------------------------------------------------
#  Motor Class
# ----------------------------------------------------------------------
    
class Motor(Energy_Component):
    
    def __defaults__(self):
        
        self.resistance         = 0.0
        self.no_load_current    = 0.0
        self.speed_constant     = 0.0
        self.propeller_radius   = 0.0
        self.propeller_Cp       = 0.0
        self.gear_ratio         = 0.0
        self.gearbox_efficiency = 0.0
        self.expected_current   = 0.0
    
    def omega(self,conditions):
        """ SUAVE.Components.Energy.Converters.Motor.omega(conditions)
            The motor's rotation rate

            Inputs:
                conditions.
                    freestream.
                        velocity [m/s]
                        density
                    propulsion.propeller_power_coefficient
            Outputs:
                The motor's rotation rate

            Properties Used:
                resistance [ohms]
                gearbox_efficiency
                expected_current [amps]
                no_load_current - Motor zeros load current [amps]
                gear_ratio
                speed_constant - Motor Kv [rad/s/volt]
                propeller_radius [m]
                inputs.voltage [V]

            Updates:
                outputs.
                    torque
                    omega

            Assumptions:
                Cp is not a function of rpm or RE

        """
        # Unpack
        V     = conditions.freestream.velocity[:,0,None]
        rho   = conditions.freestream.density[:,0,None]
        Cp    = conditions.propulsion.propeller_power_coefficient[:,0,None]
        Res   = self.resistance
        etaG  = self.gearbox_efficiency
        exp_i = self.expected_current
        io    = self.no_load_current + exp_i*(1-etaG)
        G     = self.gear_ratio
        Kv    = self.speed_constant/G
        R     = self.propeller_radius
        v     = self.inputs.voltage
    
        # Omega
        # This is solved by setting the torque of the motor equal to the torque of the prop
        # It assumes that the Cp is constant
        omega1  =   ((np.pi**(3./2.))*((- 16.*Cp*io*rho*(Kv*Kv*Kv)*(R*R*R*R*R)*(Res*Res) +
                    16.*Cp*rho*v*(Kv*Kv*Kv)*(R*R*R*R*R)*Res + (np.pi*np.pi*np.pi))**(0.5) - 
                    np.pi**(3./2.)))/(8.*Cp*(Kv*Kv)*(R*R*R*R*R)*Res*rho)
        omega1[np.isnan(omega1)] = 0.0
        
        Q = ((v-omega1/Kv)/Res -io)/Kv
        # store to outputs
       
        #P = Q*omega1
        
        self.outputs.torque = Q
        self.outputs.omega = omega1

        return omega1
    
    def current(self,conditions):
        """ SUAVE.Components.Energy.Converters.Motor.current(conditions)
            The motor's current
            
            Inputs:
                Motor resistance - in ohms
                Motor Kv - in rad/s/volt
                Voltage - volts
                Gear ratio - ~
                Rotation rate - rad/s
                
            Outputs:
                The motor's current

            Properties Used:
                gear_ratio
                speed_constant - Motor Kv [rad/s/volt]
                resistance [ohms]
                inputs.voltage [V]
                outputs.omega
                gearbox_efficiency
                expected_current [amps]
                no_load_current - Motor zeros load current [amps]

            Updates:
                outputs.current
               
            Assumptions:
                Cp is invariant
               
        """    
        
        # Unpack
        G     = self.gear_ratio
        Kv    = self.speed_constant
        Res   = self.resistance
        v     = self.inputs.voltage
        omeg  = self.outputs.omega*G
        etaG  = self.gearbox_efficiency
        exp_i = self.expected_current
        io    = self.no_load_current + exp_i*(1-etaG)
        
        i=(v-omeg/Kv)/Res
        
        # This line means the motor cannot recharge the battery
        i[i < 0.0] = 0.0

        # Pack
        self.outputs.current = i
          
        etam=(1-io/i)*(1-i*Res/v)
        conditions.propulsion.etam = etam
        
        return i

        
    