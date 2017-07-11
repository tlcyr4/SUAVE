# Constant_Dynamic_Pressure_Constant_Altitude_Loiter.py
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

class Constant_Dynamic_Pressure_Constant_Altitude_Loiter(Constant_Speed_Constant_Altitude):
    """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Dynamic_Pressure_Constant_Altitude_Loiter()
        Segment where pressure and altitude are fixed, time intervals based on time directly, not distance
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Cruise.Constant_Dynamic_Pressure_Constant_Altitude_Loiter.__defaults__()
            initializes altitude, dynamic and initialize conditions process
        """
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude         = 0.0
        self.dynamic_pressure = 1600 * Units.pascals 
        self.time             = 1.0 * Units.sec
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Cruise.Constant_Dynamic_Pressure_Constant_Altitude_Loiter.initialize_conditions


        return

