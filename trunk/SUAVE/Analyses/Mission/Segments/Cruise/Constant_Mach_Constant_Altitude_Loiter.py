# Constant_Mach_Constant_Altitude_Loiter.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Methods.Missions import Segments as Methods

from Constant_Speed_Constant_Altitude import Constant_Speed_Constant_Altitude

# Units
from SUAVE.Core import Units

# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Constant_Mach_Constant_Altitude_Loiter(Constant_Speed_Constant_Altitude):
    """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Mach_Constant_Altitude()
        Cruise segment where mach number and altitude are fixed, time intervals based directly on time
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Mach_Constant_Altitude.__defaults__()
            initializes  altitude, mach number and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude  = None
        self.mach      = 0.5 
        self.time      = 1.0 * Units.sec
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Cruise.Constant_Mach_Constant_Altitude_Loiter.initialize_conditions


        return

