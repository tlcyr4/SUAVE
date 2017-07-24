# Constant_Speed_Constant_Angle.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Descent.Constant_Speed_Constant_Angle.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                altitude_start
                altitude_end
                descent_angle
                air_speed
            state.
                initials.conditions.frames.inertial.position_vector
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
    descent_angle= segment.descent_angle
    air_speed    = segment.air_speed   
    alt0         = segment.altitude_start 
    altf         = segment.altitude_end
    t_nondim     = state.numerics.dimensionless.control_points
    conditions   = state.conditions  

    # check for initial altitude
    if alt0 is None:
        if not state.initials: raise AttributeError('initial altitude not set')
        alt0 = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]

    # discretize on altitude
    alt = t_nondim * (altf-alt0) + alt0
    
    # process velocity vector
    v_mag = air_speed
    v_x   = v_mag * np.cos(-descent_angle)
    v_z   = -v_mag * np.sin(-descent_angle)
    
    # pack conditions    
    conditions.frames.inertial.velocity_vector[:,0] = v_x
    conditions.frames.inertial.velocity_vector[:,2] = v_z
    conditions.frames.inertial.position_vector[:,2] = -alt[:,0] # z points down
    conditions.freestream.altitude[:,0]             =  alt[:,0] # positive altitude in this context