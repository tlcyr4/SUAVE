# Linear_Mach_Constant_Rate.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np
import SUAVE

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Descent.Constant_Speed_Constant_Rate.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                descent_angle
                altitude_start
                altitude_end
                mach_start
                mach_end
            state.
                initials.conditions.frames.inertial.position_vector
                numerics.dimensionless.control_points
                conditions.freestream.speed_of_sound

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
    descent_rate = segment.descent_rate
    Mo           = segment.mach_start
    Mf           = segment.mach_end
    alt0         = segment.altitude_start 
    altf         = segment.altitude_end
    t_nondim     = state.numerics.dimensionless.control_points
    conditions   = state.conditions  
    
    # Update freestream to get speed of sound
    SUAVE.Methods.Missions.Segments.Common.Aerodynamics.update_atmosphere(segment,state)
    a          = conditions.freestream.speed_of_sound    

    # check for initial altitude
    if alt0 is None:
        if not state.initials: raise AttributeError('initial altitude not set')
        alt0 = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]

    # discretize on altitude
    alt = t_nondim * (altf-alt0) + alt0
    
    # process velocity vector
    mach_number = (Mf-Mo)*t_nondim + Mo
    v_mag       = mach_number * a
    v_z         = descent_rate # z points down
    v_x         = np.sqrt( v_mag**2 - v_z**2 )
    
    # pack conditions    
    conditions.frames.inertial.velocity_vector[:,0] = v_x[:,0]
    conditions.frames.inertial.velocity_vector[:,2] = v_z
    conditions.frames.inertial.position_vector[:,2] = -alt[:,0] # z points down
    conditions.freestream.altitude[:,0]             =  alt[:,0] # positive altitude t
