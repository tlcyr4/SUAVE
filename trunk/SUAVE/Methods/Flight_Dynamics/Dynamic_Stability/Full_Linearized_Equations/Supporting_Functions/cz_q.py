# @ingroup Methods-Flight_Dynamics-Dynamic_Stability-Full_Linearized_Equations-Supporting_Functions
# cz_q.py
# 
# Created:  Jun 2014, A. Wendorff
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#   Method
# ----------------------------------------------------------------------

# @ingroup Methods-Flight_Dynamics-Dynamic_Stability-Full_Linearized_Equations-Supporting_Functions
def cz_q(cm_i):
    """ output = SUAVE.Methods.Flight_Dynamics.Dynamic_Stablity.Full_Linearized_Equations.Supporting_Functions.cz_q(cm_i) 
        Calculating the coefficient of force in the z direction with respect to the rate of change of the alpha of attack of the aircraft        
        Inputs:
                 
        Outputs:
                
        Assumptions:
        
        Source:
            J.H. Blakelock, "Automatic Control of Aircraft and Missiles" Wiley & Sons, Inc. New York, 1991, (Need page number)
    """

    # Generating Stability derivative
    cz_q  = 2. * 1.1 * cm_i
    
    return cz_q