# Common.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------
#  Unpack Unknowns
# ----------------------------------------------------------------------

def unpack_unknowns(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Common.unpack_unknowns(segment,state)
        Copy unknowns from state.unknowns to state.conditions

        Assumptions:
        N/A

        Inputs:
            state.unknowns.
                throttle
                body_angle

        Outputs:
            See Updates

        Updates:
            state.conditions.
                propulsion.throttle
                frames.body.inertial_rotations

    """
    # unpack unknowns
    throttle   = state.unknowns.throttle
    body_angle = state.unknowns.body_angle
    
    # apply unknowns
    state.conditions.propulsion.throttle[:,0]            = throttle[:,0]
    state.conditions.frames.body.inertial_rotations[:,1] = body_angle[:,0]   
    

# ----------------------------------------------------------------------
#  Residual Total Forces
# ----------------------------------------------------------------------

def residual_total_forces(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Common.residual_total_forces(segment,state)
        Copy residuals from state.conditions to state.residuals

        Assumptions:
        N/A

        Inputs:
            state.conditions.
                frames.inertial.total_force_vector
                weights.total_mass

        Outputs:
            See Updates

        Updates:
            state.residual.forces

    """
    FT = state.conditions.frames.inertial.total_force_vector
    m  = state.conditions.weights.total_mass[:,0] 
    
    # horizontal
    state.residuals.forces[:,0] = np.sqrt( FT[:,0]**2. + FT[:,1]**2. )/m
    # vertical
    state.residuals.forces[:,1] = FT[:,2]/m

    return
    
    
 
    
    