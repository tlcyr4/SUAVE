# Hover.py
#
# Created:
# Modified:

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

#import numpy as np


# ----------------------------------------------------------------------
#  Unpack Unknowns
# ----------------------------------------------------------------------

def unpack_unknowns(segment,state):
    """ SUAVE.Methods.Mission.Segments.Hover.Hover.unpack_unknowns(segment,state)
        Load unknowns into state.conditions

        Assumptions:
        N/A

        Inputs:
            state.unknowns.throttle

        Outputs:
            See Updates

        Updates:
            state.conditions.propulsion.throttle

    """
    # unpack unknowns
    throttle   = state.unknowns.throttle
    
    # apply unknowns
    state.conditions.propulsion.throttle[:,0] = throttle[:,0]
    

# ----------------------------------------------------------------------
#  Residual Total Forces
# ----------------------------------------------------------------------

def residual_total_forces(segment,state):
    """ SUAVE.Methods.Mission.Segments.Hover.Hover.residual_total_forces(segment,state)
        Load unknowns into state.conditions

        Assumptions:
        N/A

        Inputs:
            state.conditions.frames.inertial.total_force_vector

        Outputs:
            See Updates

        Updates:
            state.residuals.forces

    """
    FT = state.conditions.frames.inertial.total_force_vector

    # vertical
    state.residuals.forces[:,0] = FT[:,2]

    return
    
    
 
    
    