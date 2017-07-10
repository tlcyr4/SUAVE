# Loads.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Analyses import Analysis, Results 


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Loads(Analysis):
    """ SUAVE.Analyses.Loads.Loads()
        Base Analysis for analysing loads of a vehicle
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Loads.Loads.__defaults__()
            Sets tag to loads and initializes features and settings
        """
        self.tag    = 'loads'
        self.features = Data()
        self.settings = Data()
        
        
    def evaluate(self,condtitions):
        """ SUAVE.Analyses.Loads.Loads.evaluate()
            Run analysis-specific evaluation
            
            Inputs:
                condtitions - mispelling of conditions
                
            Outputs:
                default Results object
        """
        return Results()
        