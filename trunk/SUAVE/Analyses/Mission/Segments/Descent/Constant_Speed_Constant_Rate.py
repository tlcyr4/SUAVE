# Constant_Speed_Constant_Rate.py
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

class Constant_Speed_Constant_Rate(Unknown_Throttle):
    """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Dynamic_Pressure_Constant_Rate()
        Descent segment where air speed and descent rate are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Descent.Constant_Dynamic_Pressure_Constant_Rate.__defaults__()
            initializes end altitude, descent rate, air speed and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude_start = None # Optional
        self.altitude_end   = 10. * Units.km
        self.descent_rate   = 3.  * Units.m / Units.s
        self.air_speed      = 100 * Units.m / Units.s
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
    
        # only need to change one setup step from constant_speed_constant_rate
        initialize = self.process.initialize
        initialize.conditions = Methods.Descent.Constant_Speed_Constant_Rate.initialize_conditions
       
        return

