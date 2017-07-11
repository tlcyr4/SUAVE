# Fidelity_One.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
from Noise import Noise

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------
class Fidelity_One(Noise):
    """ SUAVE.Analyses.Noise.Noise()
        Low fidelity analysis model for noise (not implemented)
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Noise.Noise.__defaults__()
            Sets up settings
        """
        self.tag    = 'fidelity_zero_markup'              
    
        # correction factors
        settings = self.settings
        settings.flyover        = 0     
        settings.approach       = 0
        settings.sideline       = 0
        settings.mic_x_position = 0
        