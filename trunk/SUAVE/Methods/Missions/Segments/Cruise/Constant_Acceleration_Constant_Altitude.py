# Constant_Acceleration_Constant_Altitude.py
#
# Created:
# Modified:

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# N/A


# ----------------------------------------------------------------------
#  Unpack Unknowns
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Acceleration_Constant_Altitude.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                altitude
                air_speed_initial
                air_speed_final
                acceleration
            state.
                initials.conditions.frames.inertial.position_vector
                numerics.dimensionless.control_points
                conditions.frames.inertial.time

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
    alt = segment.altitude 
    v0  = segment.air_speed_initial
    vf  = segment.air_speed_final 
    ax  = segment.acceleration   
    conditions = state.conditions 
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_final   = (vf-v0)/ax + t_initial
    t_nondim  = state.numerics.dimensionless.control_points
    time      = t_nondim * (t_final-t_initial) + t_initial
    
    # Figure out vx
    vx = v0+time*ax
    
    # pack
    state.conditions.freestream.altitude[:,0] = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = vx[:,0]
    state.conditions.frames.inertial.time[:,0] = time[:,0]
    
    
    
def residual_total_forces(segment,state):
    """ SUAVE.Methods.Mission.Segments.Cruise.Constant_Acceleration_Constant_Altitude.residual_total_forces(segment,state)
        Pack up forces into state.residuals

        Assumptions:
        N/A

        Inputs:
            segment.
                state.ones_row
                acceleration
            state.
                conditions.
                    frames.inertial.total_force_vector
                    weights.total_mass

        Outputs:
            See Updates

        Updates:
            state.residuals.forces

    """
    FT      = state.conditions.frames.inertial.total_force_vector
    ax      = segment.acceleration 
    m       = state.conditions.weights.total_mass  
    one_row = segment.state.ones_row
    
    a_x    = ax*one_row(1)
    #a_x[0] = 0.
    
    # horizontal
    state.residuals.forces[:,0] = FT[:,0]/m[:,0] - a_x[:,0]
    # vertical
    state.residuals.forces[:,1] = FT[:,2]

    return
    