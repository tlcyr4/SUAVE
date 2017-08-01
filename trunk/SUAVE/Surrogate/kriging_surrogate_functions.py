# kriging_surrogate_functions.py
#
# Created:  May 2016, M. Vegh
# Modified:


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------


from SUAVE.Core import Units, Data
try:
    from pyKriging.krige import kriging  
except ImportError:
    pass 
from Surrogate_Problem import Surrogate_Problem
import numpy as np
import time


# ----------------------------------------------------------------------
#  kriging_surrogate_functions
# ----------------------------------------------------------------------



def build_kriging_models(obj_values, inputs, constraints):
    """ SUAVE.Surrogate.krigin_surrogate_functions.build_krigin_models()
        Builds pyKriging kriging object

        See pyKriging documentation

        Inputs:
            obj_values
            inputs
            constraints - array

        Outputs:
            obj_surrogate
            constrainte_surrogates
            surrogate_function
    """

    #now build surrogates based on these
    t1=time.time()
  
    
    obj_surrogate = kriging(inputs, obj_values , name='simple')
    obj_surrogate.train()
    constraints_surrogates = []
   
    
    
    for j in range(len(constraints[0,:])): 
        constraint_surrogate = kriging(inputs, constraints[:,j] , name='simple')
        constraint_surrogate.train()
        constraints_surrogates.append(constraint_surrogate)
    t2=time.time()
    print 'time to set up = ', t2-t1
    surrogate_function    = Surrogate_Problem()
    surrogate_function.obj_surrogate          = obj_surrogate
    surrogate_function.constraints_surrogates = constraints_surrogates
    
    return obj_surrogate, constraints_surrogates, surrogate_function    
    
    


