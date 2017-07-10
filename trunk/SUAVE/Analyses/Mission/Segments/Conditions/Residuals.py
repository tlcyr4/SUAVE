# Residuals.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Conditions import Conditions

# ----------------------------------------------------------------------
#  Residuals
# ----------------------------------------------------------------------

class Residuals(Conditions):
    """ SUAVE.Analyses.Mission.Segments.Residuals()
        Holds residuals (values on their way to converging to 0) from solver
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Residuals.__defaults__()
            just the tag: 'residuals', everything else depends on what's being solved
        """
        self.tag = 'residuals'