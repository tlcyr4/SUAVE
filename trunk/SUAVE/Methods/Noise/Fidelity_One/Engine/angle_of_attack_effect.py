# angle_of_attack_effect.py
# 
# Created:  Jul 2015, C. Ilario
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------        
#   Imports
# ---------------------------------------------------------------------- 

import numpy as np

# ----------------------------------------------------------------------        
#   Angle of Attack Effect
# ---------------------------------------------------------------------- 

def angle_of_attack_effect(AOA,Mach_aircraft,theta_m):
    """ SUAVE.Methods.Noise.Fidelity_One.Engine.angle_of_attack_effect(AOA,Mach_aircraft,theta_m)
        This function calculates the angle of attack effect, in decibels, to be added to the predicted mixed jet noise level.

        Inputs:
            AOA - angle of attack
            Mach_aircraft - mach-number
            theta_m

        Outputs:
            angle of attack effect [db]
    """

    #Angle of attack effect
    ATK_m = 0.5*AOA*Mach_aircraft*((1.8*theta_m/np.pi)-0.6)**2

    return(ATK_m)
