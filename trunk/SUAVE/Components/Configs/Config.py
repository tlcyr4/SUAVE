# Config.py
#
# Created:  Oct 2014, T. Lukacyzk
# Modified: Jan 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Diffed_Data

# ----------------------------------------------------------------------
#  Config
# ----------------------------------------------------------------------

class Config(Diffed_Data):
    """ SUAVE.Components.Config()
        Configurations of a vehicle/component, direct inheritance from Diffed_Data
    """
    
    def __defaults__(self):
        """ SUAVE.Components.Config.__defaults__()
            Just sets tag
        """
        self.tag    = 'config'
        

# ----------------------------------------------------------------------
#  Config Container
# ----------------------------------------------------------------------

class Container(Diffed_Data.Container):
    """ SUAVE.Components.Config.Container()
        Container of configs, direct inheritance from Diffed_Data.Container
    """
    pass

# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Config.Container = Container
