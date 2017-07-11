# Linear_Mach_Constant_Rate.py
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

class Linear_Mach_Constant_Rate(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Dynamic_Pressure_Constant_Rate()
        Descent segment where descent rate is fixed and mach number varies linearly
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Dynamic_Pressure_Constant_Rate.__defaults__()
            initializes end altitude, climb rate (mistake?), start/end mach number and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 10. * Units.km
        self.climb_rate     = 3.  * Units.m / Units.s #descent rate?
        self.mach_end    = 0.7
        self.mach_start  = 0.8
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        # only need to change one setup step from constant_speed_constant_rate
        initialize = self.process.initialize
        initialize.conditions = Methods.Descent.Linear_Mach_Constant_Rate.initialize_conditions

        return

