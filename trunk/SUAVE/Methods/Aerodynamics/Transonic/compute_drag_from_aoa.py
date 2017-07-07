# compute_drag_from_aoa.py
#
# Created:  Jul 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import numpy as np
    
# ----------------------------------------------------------------------
#   compute_drag_from_aoa
# ----------------------------------------------------------------------
def compute_drag_from_aoa(aoa):
    """ SUAVE.Methods.Aerodynamics.Transonic.compute_drag_from_aoa(aoa)
        Uses aoa to calculate cd
        
        Inputs:
            aoa - angle of attack (column array)
            
        Outputs:
            cd - drag coefficient (column array)
    """
    # model coefficients
    bd = np.array([[0.00162236444781382],	[0.000443156656073951],	[0.0141465405789619]])
    
    # calculate coefficients
    cd = bd[2] + bd[1] * aoa + bd[0] * np.square(aoa)
    
    return cd