# Constant_Mach_Constant_Angle.py
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

class Constant_Mach_Constant_Angle(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Mach_Constant_Angle()
        Climb segment where mach number and climb angle are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Climb.Constant_Mach_Constant_Angle.__defaults__()
            initializes start/end altitude, climb angle, mach number and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 10. * Units.km
        self.climb_angle    = 3.  * Units.deg
        self.mach           = 0.7
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        # only need to change one setup step from constant_speed_constant_ate
        initialize = self.process.initialize
        initialize.conditions = Methods.Climb.Constant_Mach_Constant_Angle.initialize_conditions
        
       
        return

