# Hover.py
#
# Created:
# Modified:

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

#import numpy as np

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Hover.Hover.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                time
                altitude

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
                freestream.altitude

    """
    # unpack
    alt        = segment.altitude
    duration   = segment.time
    conditions = state.conditions   
    
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt        
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_nondim  = state.numerics.dimensionless.control_points
    time      =  t_nondim * (duration) + t_initial
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = 0.
    state.conditions.frames.inertial.time[:,0]            = time[:,0]    