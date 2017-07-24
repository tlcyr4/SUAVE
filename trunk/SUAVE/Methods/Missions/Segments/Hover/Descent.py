# Descent.py
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

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Hover.Descent.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                descent_rate
                altitude_start
                altitude_end

            state.
                initials.conditions.frames.inertial.position_vector
                conditions.frames.inertial.time
                numerics.dimensionless.control_points

        Outputs:
            See Updates

        Updates:
            state.conditions.
                frames.inertial.
                    position_vector
                    velocity_vector
                    time
                freestream.altitude

    """
    # unpack
    descent_rate = segment.descent_rate
    alt0       = segment.altitude_start 
    altf       = segment.altitude_end
    t_nondim   = state.numerics.dimensionless.control_points
    t_initial  = state.conditions.frames.inertial.time[0,0]
    conditions = state.conditions  

    # check for initial altitude
    if alt0 is None:
        if not state.initials: raise AttributeError('initial altitude not set')
        alt0 = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]

    # discretize on altitude
    alt = t_nondim * (altf-alt0) + alt0
    
    # process velocity vector
    v_z = descent_rate # z points down    
    dt  = (alt0 - altf)/descent_rate

    # rescale operators
    t = t_nondim * dt

    # pack
    t_initial = state.conditions.frames.inertial.time[0,0]
    state.conditions.frames.inertial.time[:,0] = t_initial + t[:,0]    
    
    # pack conditions    
    conditions.frames.inertial.velocity_vector[:,0] = 0.
    conditions.frames.inertial.velocity_vector[:,2] = v_z
    conditions.frames.inertial.position_vector[:,2] = -alt[:,0] # z points down
    conditions.freestream.altitude[:,0]             =  alt[:,0] # positive altitude in this context
    state.conditions.frames.inertial.time[:,0]      = t_initial + t[:,0]