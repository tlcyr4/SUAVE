# Sizing.py
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

class Sizing(Analysis):
    """ SUAVE.Analyses.Sizing.Sizing()
        Base analysis model for analysing planets
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Sizing.Sizing.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'sizing'
        self.features = Data()
        self.settings = Data()
        
        
    def evaluate(self,conditions):
        """ SUAVE.Analyses.Sizing.Sizing.evaluate()
            Runs sizing analysis (analysis-specific)
        """
        return Results()
    
    __call__ = evaluate
        