# Constant_Speed_Constant_Angle_Noise.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
import SUAVE

from SUAVE.Methods.Missions import Segments as Methods

from SUAVE.Analyses.Mission.Segments.Climb.Unknown_Throttle import Unknown_Throttle

# Units
from SUAVE.Core import Units


# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Constant_Speed_Constant_Angle_Noise(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Speed_Constant_Angle_Noise()
        Descent segment where air speed and descent angle are fixed, start position determined by descent angle
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Speed_Constant_Angle_Noise.__defaults__()
            initializes end altitude, descent angle, air speed and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 0.0 * Units.km
        self.descent_angle  = 3.  * Units.deg
        self.air_speed      = 100 * Units.m / Units.s
        self.state.numerics.discretization_method = SUAVE.Methods.Utilities.Chebyshev.linear_data
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        initialize = self.process.initialize
        initialize.conditions   = Methods.Descent.Constant_Speed_Constant_Angle_Noise.initialize_conditions
        initialize.expand_state = Methods.Descent.Constant_Speed_Constant_Angle_Noise.expand_state
        
        return

