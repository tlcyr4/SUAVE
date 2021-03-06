# Constant_Mach_Constant_Altitude.py
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

class Constant_Mach_Constant_Altitude(Constant_Speed_Constant_Altitude):
    """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Mach_Constant_Altitude()
        Cruise segment where mach number and altitude are fixed
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Mach_Constant_Altitude.__defaults__()
            initializes altitude, mach number and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude  = None
        self.mach      = 0.5 
        self.distance  = 10. * Units.km
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Cruise.Constant_Mach_Constant_Altitude.initialize_conditions


        return

