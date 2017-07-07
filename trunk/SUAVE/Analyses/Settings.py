# Settings.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Core import Container as ContainerBase


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Settings(Data):
    """ SUAVE.Analyses.Settings()
        settings for execution of simulation
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Settings.__defaults__()
            updates tag and sets verbose to false
        """
        self.tag    = 'settings'
        
        self.verbose_process = False
        

# ----------------------------------------------------------------------
#  Config Container
# ----------------------------------------------------------------------

class Container(ContainerBase):
    """ SUAVE.Analyses.Settings.Container()
        container of settings
    """
    

# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Settings.Container = Container