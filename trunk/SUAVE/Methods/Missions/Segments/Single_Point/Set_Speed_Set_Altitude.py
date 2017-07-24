# Set_Speed_Set_Altitude.py
# 
# Created:  Mar 2017, T. MacDonald
# Modified: 

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Single_Point.Set_Speed_Set_Altitude.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            segment.
                air_speed
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
            segment.altitude

    """
    # unpack
    alt        = segment.altitude
    air_speed  = segment.air_speed       
    conditions = state.conditions 
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = air_speed
    
def update_weights(segment,state):
    """ SUAVE.Methods.Mission.Segments.Single_Point.Set_Speed_Set_Altitude.update_weights(segment,state)
        Set up initial conditions of state.conditions

        Assumptions:
        N/A

        Inputs:
            state.conditions.
                weights.total_mass
                freestream.gravity

        Outputs:
            See Updates

        Updates:
            state.conditions.frames.inertial.gravity_force_vector

    """
    # unpack
    conditions = state.conditions
    m0         = conditions.weights.total_mass[0,0]
    g          = conditions.freestream.gravity

    # weight
    W = m0*g

    # pack
    conditions.frames.inertial.gravity_force_vector[:,2] = W

    return