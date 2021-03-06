# scikit_surrogate_functions.py
#
# Created:  May 2016, M. Vegh
# Modified:


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------


from SUAVE.Core import Data
from Surrogate_Problem import Surrogate_Problem

import numpy as np
import time

# ----------------------------------------------------------------------
#  read_sizing_inputs
# ----------------------------------------------------------------------


def build_scikit_models(surrogate_optimization, obj_values, inputs, constraints):
    """ SUAVE.Surrogate.krigin_surrogate_functions.build_krigin_models()
        Builds scikit kriging object

        See scikit documentation

        Inputs:
            surrogate_optimization
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
    regr = surrogate_optimization.surrogate_model()
    obj_surrogate = regr.fit(inputs, obj_values)
    constraints_surrogates = []
    #now run every constraint
    for j in range(len(constraints[0,:])):
        regr = surrogate_optimization.surrogate_model()
        constraint_surrogate = regr.fit(inputs, constraints[:,j]) 
        constraints_surrogates.append(constraint_surrogate)
     
    t2=time.time()
    print 'time to set up = ', t2-t1
    surrogate_function                        = Surrogate_Problem()
    surrogate_function.obj_surrogate          = obj_surrogate
    surrogate_function.constraints_surrogates = constraints_surrogates
    
    return obj_surrogate, constraints_surrogates, surrogate_function    
    


