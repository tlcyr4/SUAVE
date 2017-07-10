# Geometry.py
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

class Geometry(Analysis):
    """ SUAVE.Analyses.Geometry.Geometry()
        Base analysis for analysing geometry of a vehicle
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Geometry.Geometry.__defaults__()
            Sets tag to geometry and initializes features and settings
        """
        self.tag    = 'geometry'
        self.features = Data()
        self.settings = Data()
        
        
    def evaluate(self,condtitions):
        """ SUAVE.Analyses.Geometry.Geometry.evaluate()
            Run analysis-specific evaluation
            
            Inputs:
                condtitions - mispelling of conditions
                
            Outputs:
                default Results object
        """
        return Results()
    
        