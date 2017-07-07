# compute_lift.py
#
# Created:  Jul 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import numpy as np
    
# ----------------------------------------------------------------------
#   compute_lift
# ----------------------------------------------------------------------
def compute_lift(aoa):
    """ SUAVE.Method.Aerodynamics.Transonic.compute_lift(aoa)
        Uses aoa to calculate cl  quadratic curve fits
        
        Inputs:
            aoa - angle of attack (column array)
            
        Outputs:
            cl - lift coefficient (column array)
    """
    # model coefficients
    bl = np.array([[-0.00717433179381432],	[0.144047701950893],	[0.126479444126983]])
    
    # calculate coefficients
    cl = bl[2] + bl[1] * aoa + bl[0] * np.square(aoa)
    
    return cl