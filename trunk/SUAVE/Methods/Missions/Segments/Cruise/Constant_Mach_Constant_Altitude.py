# Constant_Mach_Constant_Altitude.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Mach_Constant_Altitude.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                altitude
                distance
                mach
            state.
                initials.conditions.frames.inertial.position_vector
                numerics.dimensionless.control_points
                conditions.freestream.speed_of_sound

        Outputs:
            See Updates

        Updates:
            state.conditions.
                freestream.altitude
                frames.inertial.
                    position_vector
                    velocity_vector
                    time
            segment.altitude

    """
    # unpack
    alt        = segment.altitude
    xf         = segment.distance
    mach       = segment.mach
    conditions = state.conditions   
    
    # Update freestream to get speed of sound
    SUAVE.Methods.Missions.Segments.Common.Aerodynamics.update_atmosphere(segment,state)
    a          = conditions.freestream.speed_of_sound    
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt        
    
    # compute speed, constant with constant altitude
    air_speed = mach * a
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_final   = xf / air_speed + t_initial
    t_nondim  = state.numerics.dimensionless.control_points
    time      =  t_nondim * (t_final-t_initial) + t_initial
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = air_speed[:,0]
    state.conditions.frames.inertial.time[:,0]            = time[:,0]
    
