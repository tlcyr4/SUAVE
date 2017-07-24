# Constant_Dynamic_Pressure_Constant_Altitude.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
import numpy as np

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Dynamic_Pressure_Constant_Altitude.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                altitude
                distance
                dynamic_pressure
            state.
                initials.conditions.frames.inertial.position_vector
                numerics.dimensionless.control_points
                conditions.freestream.density

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
    q          = segment.dynamic_pressure
    conditions = state.conditions   
    
    # Update freestream to get density
    SUAVE.Methods.Missions.Segments.Common.Aerodynamics.update_atmosphere(segment,state)
    rho        = conditions.freestream.density[:,0]   
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt        
    
    # compute speed, constant with constant altitude
    air_speed = np.sqrt(q/(rho*0.5))
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_final   = xf / air_speed + t_initial
    t_nondim  = state.numerics.dimensionless.control_points
    time      = t_nondim * (t_final-t_initial) + t_initial
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = air_speed
    state.conditions.frames.inertial.time[:,0]            = time[:,0]