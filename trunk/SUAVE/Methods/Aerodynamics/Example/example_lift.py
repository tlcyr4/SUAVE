# example_lift.py
# 
# Created:  Jun 2017, Tigar Cyr
# Modified: 

## style note --
## this is a stand alone method, and should be lower_case_with_underscore

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
#  Example Lift
# ----------------------------------------------------------------------

def example_lift(segment, state):
    """ SUAVE.Methods.Example.example_lift(segment, state)
        calculates lift based on NACA 0012 (poorly)
        
        Inputs:
            segment - mission segment currently being evaluated
            state - state of the system
            
        Outputs:
            lift_coefficient - lift coefficient of the vehicle
    """
    
    # unpack input
    alpha = state.conditions.aerodynamics.angle_of_attack
    
    # calculate lift coefficient
    cl = 1.25 / 12 * alpha
    
    # correct for stall
    # Note: inputs and outputs are numpy arrays
    for index in range(len(alpha)):
        if alpha[index] > 12.:
            cl[index] = 2 - .25/3 * alpha
    
    return cl
    
        
