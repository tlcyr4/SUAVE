# Constant_Speed_Constant_Angle.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Methods.Missions import Segments as Methods

from SUAVE.Analyses.Mission.Segments.Climb.Unknown_Throttle import Unknown_Throttle

# Units
from SUAVE.Core import Units


# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Constant_Speed_Constant_Angle(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Speed_Constant_Angle()
        Descent segment where air speed and descent angle are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Speed_Constant_Angle.__defaults__()
            initializes end altitude, descent angle, air speed and initializes initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 0.0 * Units.km
        self.descent_angle  = 3.  * Units.deg
        self.air_speed      = 100 * Units.m / Units.s
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        # only need to change one setup step from constant_speed_constant_rate
        initialize = self.process.initialize
        initialize.conditions = Methods.Descent.Constant_Speed_Constant_Angle.initialize_conditions
       
        return

