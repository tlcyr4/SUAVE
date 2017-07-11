# Takeoff.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from Ground import Ground
from SUAVE.Methods.Missions import Segments as Methods

# Units
from SUAVE.Core import Units

# ----------------------------------------------------------------------
#  Class
# ----------------------------------------------------------------------

class Takeoff(Ground):
    """ SUAVE.Analyses.Mission.Segments.Ground.Landing()
        Segment for aircraft takeoffs
    """
    # ------------------------------------------------------------------
    #   Data Defaults
    # ------------------------------------------------------------------  
    
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Ground.Landing.__defaults__()
            initializes start and end velocity, friction coefficient, throttle and conditions initialization
        """
        self.velocity_start       = 0.0
        self.velocity_end         = 150 * Units.knots
        self.friction_coefficient = 0.04
        self.throttle             = 1.0

        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        initialize = self.process.initialize
        initialize.conditions = Methods.Ground.Takeoff.initialize_conditions
        
        return


