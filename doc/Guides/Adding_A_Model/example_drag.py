# example_drag.py
# 
# Created:  Jun 2017, Tigar Cyr
# Modified: 

## style note --
## this is a stand alone method, and should be lower_case_with_underscore

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
#  Example Drag
# ----------------------------------------------------------------------

def example_drag(segment, state):
    """ SUAVE.Methods.Example.example_drag(segment, state)
        calculates drag based on NACA 0012 (poorly)
        
        Inputs:
            segment - mission segment currently being evaluated
            state - state of the system
            
        Outputs:
            drag_coefficient - drag coefficient of the vehicle
    """
    
    # unpack input
    alpha = state.conditions.aerodynamics.angle_of_attack
    
    # calculate drag coefficient
    cd = alpha ** 2 + 0.1
    
    return cd
    
        
