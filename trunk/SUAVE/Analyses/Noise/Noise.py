# Noise.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Analyses import Analysis

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Noise(Analysis):
    """ SUAVE.Analyses.Noise.Noise()
        Base analysis for analysing noise made by vehicle
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Noise.Noise.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'aerodynamics'
        
        self.geometry = Data()
        self.settings = Data()
        
        
    def evaluate(self,state):
        """ SUAVE.Analyses.Noise.Noise.evaluate(state)
            evaluates model and returns results (analysis-specific)
            
            Inputs:
                state - state of the system
                
            Outputs:
                results - datadict object with results of analysis
        """
        
        results = Data()
        
        return results
    
    def finalize(self):
        """ SUAVE.Analyses.Noise.Noise.finalize()
            analysis specific finalization
        """
        return  