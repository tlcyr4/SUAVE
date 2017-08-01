# surrogate_problem.py
#
# Created:  May 2016, M. Vegh
# Modified:


from SUAVE.Core import Data
import numpy as np


# ----------------------------------------------------------------------
#  Surrogate_Problem
# ----------------------------------------------------------------------


class Surrogate_Problem(Data):
    def __defaults__(self):
        """ SUAVE.Surrogate.Surrogate_Problem.__defaults__()
            Sets default values

            Updates:
                self.
                    obj_surrogate - data object
                    constraints_surrogates - constraints
        """
        self.obj_surrogate = None
        self.constraints_surrogates = None
    
    def compute(self, x):
        """ SUAVE.Surrogate.Surrogate_Problem.__defaults__()
            Computes surrogate predictions

            Inputs:
                x - point to be examined

            Outputs:
                f - output from surrogate object
                g - output from constraints
                fail - did either one produce and NaNs
        """
        f = self.obj_surrogate.predict(x)
        g = []
        for j in range(len(self.constraints_surrogates)):
            g.append(self.constraints_surrogates[j].predict(x))
          
        #g = np.array(g) #uncomment if particular surrogate saves each value as array
        
        fail  = np.array(np.isnan(f.tolist()) or np.isnan(np.array(g).any())).astype(int)
    
        return f, g, fail
        
    __call__ = compute