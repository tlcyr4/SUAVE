# Results
# Created:   Trent, Jan 2014
# Modified:  Andrew Wendorff, Feb 2016

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Analyses import Results as Base_Results
import numpy as np

# ----------------------------------------------------------------------
#  Default Aerodynamic Results
# ----------------------------------------------------------------------


default_result = np.zeros([1,1])

class Results(Base_Results):
    """ SUAVE.Analyses.Aerodynamics.Results()
        Default results for aerodynamic analysis
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Aerodynamics.Results.__defaults__()
            lift and force coefficient and force vectors default to [[0]]
        """
        self.lift_coefficient  = default_result * 0.
        self.drag_coefficient  = default_result * 0.
        
        self.lift_force_vector = default_result * 0.
        self.drag_force_vector = default_result * 0.
