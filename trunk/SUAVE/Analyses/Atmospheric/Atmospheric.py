## @ingroup analyses-atmospheric
# Atmospheric.py
#
# Created:  Feb 2015, T. MacDonald
# Modified: Feb 2016, A. Wendorff


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Attributes.Atmospheres.Atmosphere import Atmosphere
from SUAVE.Analyses import Analysis


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

## @ingroup analyses-atmospheric
class Atmospheric(Analysis):
    """ SUAVE.Analyses.Atmospheric.Atmospheric()
        This is the base class for atmospheric analyses.
    
        Assumptions:
        None
        
        Source:
        N/A
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Atmospheric.Atmospheric.__defaults__()
            Initializes with default atmosphere properties.  See Atmosphere.py.
            
            Assumptions:
            None
            
            Source:
            N/A
            
            Inputs:
            None
            
            Outputs:
            None
            
            Properties Used:
            None.
        """          
        atmo_data = Atmosphere()
        self.update(atmo_data)
        
        
    def compute_values(self,altitude):
        """ SUAVE.Analyses.Atmospheric.Atmospheric.altitude(altitude)
            This function is not implemented.
        """
        raise NotImplementedError
