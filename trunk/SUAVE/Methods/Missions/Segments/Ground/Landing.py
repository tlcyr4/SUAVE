# Landing.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import Common

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------   

def initialize_conditions(segment,state):
    """ SUAVE.Methods.Mission.Segments.Ground.Landing.initialize_conditions(segment,state)
        Set up initial conditions of state.conditions
        See Common.initialize_conditions
        Rest of docstring is about affects in addition to that

        Assumptions:
        N/A

        Inputs:
            segment.
                analyses.weights.vehicle.mass_properties.landing
                throttle
        Outputs:
            See Updates

        Updates:
            state.conditions.
                weights.total_mass
                propulsion.throttle

    """
    Common.initialize_conditions(segment,state)
    
    m_initial = segment.analyses.weights.vehicle.mass_properties.landing
          
    # apply initials
    conditions = state.conditions
    conditions.weights.total_mass[:,0] = m_initial

    throttle = segment.throttle	
    conditions.propulsion.throttle[:,0] = throttle        

    return conditions