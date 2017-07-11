# Constant_Speed_Constant_Angle.py
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

class Constant_Speed_Constant_Angle(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Speed_Constant_Angle()
        Climb segment where air speed and climb angle are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Speed_Constant_Angle.__defaults__()
            initializes end altitude, climb angle, air speed and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 10. * Units.km
        self.climb_angle    = 3.  * Units.deg
        self.air_speed      = 100 * Units.m / Units.s
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Climb.Constant_Speed_Constant_Angle.initialize_conditions
    
        return
       