# Stability.py
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

class Stability(Analysis):
    """ SUAVE.Analyses.Stability.Stability()
        Base analysis for analysing aircraft stability
    """
    
    def __defaults__(self):
        """ SUAVE.Analyses.Stability.Stability.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'stability'
        self.geometry = Data()
        self.settings = Data()
        
    def evaluate(self,conditions):
        """ SUAVE.Analyses.Stability.Stability.evaluate()
            Runs stability analysis (analysis-specific)
            
            Inputs:
                conditions - conditions of the system
        """
        results = Results()
        
        return results
    
    
    def finalize(self):
        """ SUAVE.Analyses.Stability.Stability.finalize()
            analysis specific finalization
        """
        
        return
    
    
        