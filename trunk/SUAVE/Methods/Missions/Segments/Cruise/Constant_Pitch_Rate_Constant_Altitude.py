# Constant_Pitch_Rate_Constant_Altitude.py
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

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Pitch_Rate_Constant_Altitude.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                altitude
                pitch_initial
                pitch_final
                pitch_rate
            state.
                initials.conditions.
                    frames.inertial.position_vector
                    body.inertial_rotations
                numerics.dimensionless.control_points
                conditions.
                    freestream.speed_of_sound
                    frames.inertial.time

        Outputs:
            See Updates

        Updates:
            state.conditions.
                freestream.altitude
                frames.
                    body.inertial_rotations
                    inertial.
                        position_vector
                        time
            segment.
                altitude
                pitch_initial

    """
    # unpack
    alt        = segment.altitude 
    T0         = segment.pitch_initial
    Tf         = segment.pitch_final 
    theta_dot  = segment.pitch_rate   
    conditions = state.conditions 
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt
        
    # check for initial pitch
    if T0 is None:
        T0  =  state.initials.conditions.frames.body.inertial_rotations[-1,1]
        segment.pitch_initial = T0
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_final   = (Tf-T0)/theta_dot + t_initial
    t_nondim  = state.numerics.dimensionless.control_points
    time      = t_nondim * (t_final-t_initial) + t_initial
    
    # set the body angle
    body_angle = theta_dot*time + T0
    state.conditions.frames.body.inertial_rotations[:,1] = body_angle[:,0]    
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.time[:,0]            = time[:,0]
    
    
    
def residual_total_forces(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Pitch_Rate_Constant_Altitude.residual_total_forces(segment,state)
        Calculate residual forces

        Assumptions:
        N/A

        Inputs:
            state.
                numerics.time.differentiate
                conditions.
                    freestream.speed_of_sound
                    frames.inertial.
                        total_force_vector
                        velocity_vector
                        acceleration_vector
                    weights.total_mass

        Outputs:
            See Updates

        Updates:
            state.
                conditions.
                    frames.inertial.acceleration_vector
                residuals.forces
    """
    FT = state.conditions.frames.inertial.total_force_vector
    m  = state.conditions.weights.total_mass  
    v  = state.conditions.frames.inertial.velocity_vector
    D  = state.numerics.time.differentiate
    m  = state.conditions.weights.total_mass    
    
    # process and pack
    acceleration = np.dot(D,v)
    state.conditions.frames.inertial.acceleration_vector = acceleration
    a  = state.conditions.frames.inertial.acceleration_vector
    
    # horizontal
    state.residuals.forces[:,0] = FT[:,0]/m[:,0] - a[:,0]
    # vertical
    state.residuals.forces[:,1] = FT[:,2]  - a[:,2]

    return

def unpack_unknowns(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Pitch_Rate_Constant_Altitude.unpack_unknowns(segment,state)
        Load unknowns in to state.conditions

        Assumptions:
        N/A

        Inputs:
            state.unknowns.
                throttle
                velocity

        Outputs:
            See Updates

        Updates:
            state.conditions.
                propulsion.throttle
                frames.inertial.velocity_vector
    """
    # unpack unknowns
    throttle  = state.unknowns.throttle
    air_speed = state.unknowns.velocity
    
    # apply unknowns
    state.conditions.propulsion.throttle[:,0]             = throttle[:,0]
    state.conditions.frames.inertial.velocity_vector[:,0] = air_speed[:,0]
    
    