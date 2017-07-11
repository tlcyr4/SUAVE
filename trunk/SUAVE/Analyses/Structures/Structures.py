# Structures.py
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

class Structures(Analysis):
    """ SUAVE.Analyses.Structures.Structures()
        Base analysis for analysing aircraft structures
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Structures.Structures.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'structures'
        self.features = Data()
        self.settings = Data()
        
        
    def evaluate(self,conditions):
        """ SUAVE.Analyses.Structures.Structures.evaluate()
            Runs stability analysis (analysis-specific)
            
            Inputs:
                conditions - conditions of the system
        """
        return Results()
    
    __call__ = evaluate
        