# compute_drag_from_lift.py
#
# Created:  Jul 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import numpy as np
    
# ----------------------------------------------------------------------
#   compute_drag_from_lift
# ----------------------------------------------------------------------
def compute_drag_from_lift(cl):
    """ SUAVE.Methods.Aerodynamics.Transonic.compute_drag_from_lift(cl)
        Uses cl to calculate cd
        
        Inputs:
            cl - lift coefficient (column array)
            
        Outputs:
            cd - drag coefficient (column array)
    """
    # model coefficients
    bd = np.array([[0.177990108978307],	[0.04257289502394],	[0.010275150311500]])
    
    # calculate coefficients
    cd = bd[2] + bd[1] * cl + bd[0] * np.square(cl)
    
    return cd