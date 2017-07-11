# Linear_Speed_Constant_Rate.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Methods.Missions import Segments as Methods

from Unknown_Throttle import Unknown_Throttle

# Units
from SUAVE.Core import Units


# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Linear_Speed_Constant_Rate(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Climb.Linear_Speed_Constant_Rate()
        Climb segment where climb rate is fixed and air speed is changing in a fixed linear manner
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Climb.Linear_Speed_Constant_Rate.__defaults__()
            initializes end altitude, climb rate, start and end air speed and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start  = None # Optional
        self.altitude_end    = 10. * Units.km
        self.climb_rate      = 3.  * Units.m / Units.s
        self.air_speed_start = 100 * Units.m / Units.s
        self.air_speed_end   = 200 * Units.m / Units.s
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Climb.Linear_Speed_Constant_Rate.initialize_conditions

        

        return

