# Motor_Lo_Fid.py
#
# Created:  Jun 2014, E. Botero
# Modified: Jan 2016, T. MacDonald 

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE

# package imports
from SUAVE.Components.Energy.Energy_Component import Energy_Component

# ----------------------------------------------------------------------
#  Motor Class
# ----------------------------------------------------------------------
    
class Motor_Lo_Fid(Energy_Component):
    
    def __defaults__(self):
        
        self.resistance         = 0.0
        self.no_load_current    = 0.0
        self.speed_constant     = 0.0
        self.gear_ratio         = 0.0
        self.gearbox_efficiency = 0.0
        self.expected_current   = 0.0
        self.motor_efficiency   = 0.0
    
    def omega(self,conditions):
        """ SUAVE.Components.Energy.Converters.Motor_Lo_Fid.omega(conditions)
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
                motor_efficiency
                inputs.voltage [V]

            Updates:
                outputs.
                    torque
                    omega

            Assumptions:
                Cp is invariant

        """
        # Unpack
        V     = conditions.freestream.velocity[:,0,None]
        rho   = conditions.freestream.density[:,0,None]
        Res   = self.resistance
        etaG  = self.gearbox_efficiency
        exp_i = self.expected_current
        io    = self.no_load_current + exp_i*(1-etaG)
        G     = self.gear_ratio
        Kv    = self.speed_constant/G
        etam  = self.motor_efficiency
        v     = self.inputs.voltage
        

        # Omega
        omega1 = (Kv*v)/2 + (Kv*(Res*Res*io*io - 2*Res*etam*io*v - 2*Res*io*v + etam*etam*v*v - 2*etam*v*v + v*v)**(1/2))/2 - (Kv*Res*io)/2 + (Kv*etam*v)/2
        Q = ((v-omega1/Kv)/Res -io)/Kv
        
        omega1[v==0] = 0.

        # store to outputs
        self.outputs.omega  = omega1
        self.outputs.torque = Q
        
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
                omega [function]
                gearbox_efficiency
                expected_current [amps]
                no_load_current - Motor zeros load current [amps]

            Updates:
                outputs.current
               
            Assumptions:
                Cp is invariant
               
        """    
        
        # Unpack
        G    = self.gear_ratio
        Kv   = self.speed_constant
        Res  = self.resistance
        v    = self.inputs.voltage
        omeg = self.omega(conditions)*G
        etaG = self.gearbox_efficiency
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