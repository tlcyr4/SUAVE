# Linear_Mach_Constant_Rate.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Methods.Missions import Segments as Methods

from .Unknown_Throttle import Unknown_Throttle

# Units
from SUAVE.Core import Units


# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Linear_Mach_Constant_Rate(Unknown_Throttle):
    
    def __defaults__(self):
        
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 10. * Units.km
        self.climb_rate     = 3.  * Units.m / Units.s
        self.mach_end    = 0.7
        self.mach_start  = 0.8
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        # only need to change one setup step from constant_speed_constant_rate
        initialize = self.process.initialize
        initialize.conditions = Methods.Climb.Linear_Mach_Constant_Rate.initialize_conditions

        

        return

