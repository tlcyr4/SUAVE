# Planet.py
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

class Planet(Analysis):
    """ SUAVE.Analyses.Planet.Planet()
        Base analysis model for analysing planets
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Planet.Planet.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'planet'
        self.features = Data()
        self.settings = Data()
        
        from SUAVE.Attributes.Planets.Earth import Earth
        self.features = Earth()
        
        
        