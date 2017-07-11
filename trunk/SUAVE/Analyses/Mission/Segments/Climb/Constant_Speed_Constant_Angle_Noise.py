# Constant_Speed_Constant_Angle_Noise.py
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

class Constant_Speed_Constant_Angle_Noise(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Speed_Constant_Angle_Noise()
        Climb segment where air speed, noise and climb angle are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Speed_Constant_Angle_Noise.__defaults__()
            initializes end altitude, climb angle, air speed and initialize conditions process
            also expands state to incorporate microphone
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
        initialize.expand_state = Methods.Climb.Constant_Speed_Constant_Angle_Noise.expand_state        
        initialize.conditions = Methods.Climb.Constant_Speed_Constant_Angle_Noise.initialize_conditions
    
        return
       