# vortex_lift.py
# 
# Created:  Jun 2014, T. Macdonald
# Modified: Jul 2014, T. Macdonald
#           Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------
#   The Function
# ----------------------------------------------------------------------


def vortex_lift(state,settings,geometry):
    # Based on http://adg.stanford.edu/aa241/highlift/sstclmax.html
    """ SUAVE.Methods.Aerodynamics.Supersonic_Zero.Lift.vortex_lift(state,settings,geometry)
        computes the vortex lift associated with an aircraft 
        
        Inputs:
            state.conditions. - data dictionary with fields:
                freestream.
                    mach_number - float or 1D array of freestream mach numbers
                aerodynamics.
                    angle_of_attack - floar or 1D array of angle of attacks
                
            settings - data dictionary with fields:
                fuselage_lift_correction - the correction to fuselage contribution to lift
                    
            geometry - used for wing
            
        
        Outputs:
            wings_lift - float or 1D array of lift coefficients of the total aircraft
        
        Updates:
            state.conditions.aerodynamics.lift_breakdown.vortex_lift - stores results here
        
    """  

    Mc         = state.conditions.freestream.mach_number
    AoA        = state.conditions.aerodynamics.angle_of_attack
    wings_lift = state.conditions.aerodynamics.lift_coefficient
    vortex_cl  = np.array([[0.0]] * len(Mc))

    for wing in geometry.wings:

        if wing.vortex_lift is True:
            AR = wing.aspect_ratio
            GAMMA = wing.sweeps.quarter_chord
            
            # angle of attack
            a = AoA[Mc < 1.0]
            
            # lift coefficient addition
            vortex_cl[Mc < 1.0] += np.pi*AR/2*np.sin(a)*np.cos(a)*(np.cos(a)+np.sin(a)*np.cos(a)/np.cos(GAMMA)-np.sin(a)/(2*np.cos(GAMMA)))
    
    
    wings_lift[Mc <= 1.05] = wings_lift[Mc <= 1.05] + vortex_cl[Mc <= 1.05] # updates conditions.lift_coefficient 
    
    state.conditions.aerodynamics.lift_breakdown.vortex_lift = vortex_cl   
    
    return wings_lift