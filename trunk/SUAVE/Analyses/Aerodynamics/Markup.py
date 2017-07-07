# Markup.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from Aerodynamics import Aerodynamics
from SUAVE.Analyses import Process

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Markup(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Markup()
        Base aerodynamic model with an object oriented process hierarchy
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Aerodynamics.Markup.__defaults__()
            initializes tag, geometry and settings; begins initializing process hierarchy
        """
        self.tag    = 'aerodynamics_markup'
        
        self.geometry = Data()
        self.settings = Data()
        
        self.process = Process()
        self.process.initialize = Process()
        self.process.compute = Process()
        
        
    def evaluate(self,state):
        """ SUAVE.Analyses.Aerodynamics.Markup.evaluate(state)
            executes analysis specific compute subprocess
            
            Inputs:
                state - state of the system
                
            Outputs:
                results - results of the analysis
        """
        
        settings = self.settings
        geometry = self.geometry
        
        results = self.process.compute(state,settings,geometry)
        
        return results
        
    def initialize(self):
        """ SUAVE.Analyses.Aerodynamics.Markup.initialize()
            calls analysis specific initialization
        """
        self.process.initialize(self)
    
        
        