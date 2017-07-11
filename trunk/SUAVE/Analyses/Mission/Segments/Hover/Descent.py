
# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
import SUAVE
from SUAVE.Analyses.Mission.Segments import Aerodynamic
from SUAVE.Analyses.Mission.Segments import Conditions

from SUAVE.Methods.Missions import Segments as Methods

from SUAVE.Analyses import Process
from Hover import Hover

# Units
from SUAVE.Core import Units

# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Descent(Hover):
    """ SUAVE.Analyses.Mission.Segments.Hover.Descent()
        Hover segment: assumes vehicle moves down but not necessarily horizontally
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Hover.Descent.__defaults__()
            initializes end altitude and descent rate and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 1. * Units.km
        self.descent_rate   = 1.  * Units.m / Units.s
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        iterate    = self.process.iterate
        
        initialize.conditions = Methods.Hover.Descent.initialize_conditions
    
        return
       