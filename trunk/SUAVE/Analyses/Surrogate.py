# Surrogate.py
#
# Created:  Trent Lukaczyk, March 2015 
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# imports

from SUAVE.Core import Data
from Analysis import Analysis


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Surrogate(Analysis):
    ''' SUAVE.Analyses.Surrogate()
        Surrogate Model Base Class
    '''
    
    def __defaults__(self):
        """ SUAVE.Analyses.Surrogate.__defaults__()
            initializes training and surrogates variables
        """
        self.training = Data()
        self.surrogates = Data()
        return

    def finalize(self):
        """ SUAVE.Analyses.Surrogate.finalize()
            trains and builds surrogate model
        """
        self.sample_training()
        self.build_surrogate()
        return

    def sample_training(self):
        """ SUAVE.Analyses.Surrogate.sample_training()
            trains surrogate model based off of sample data
        """
        return

    def build_surrogate(self):
        """ SUAVE.Analyses.Surrogate.build_surrogate()
            builds surrogate model
        """
        return

    def evaluate(self,state):
        """ SUAVE.Analyses.Surrogate.evaluate()
            evaluate model
            
            Inputs:
                state - state of the system
                
            Outputs:
                results - results of evaluation (None by default)
        """
        results = None
        raise NotImplementedError
        return results

