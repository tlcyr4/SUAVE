#Atmosphere.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Attributes.Constants import Constant #, Composition
from SUAVE.Core import Data


# ----------------------------------------------------------------------
#  Atmosphere Class
# ----------------------------------------------------------------------

class Atmosphere(Constant):

    """ SUAVE.Attributes.Atmospheres.Atmosphere()
        Constant-property atmosphere model
    """

    def __defaults__(self):
        """ SUAVE.Attributes.Atmospheres.Atmosphere.__defaults__()
            sets tag and composition
        """
        self.tag = 'Constant-property atmosphere'
        self.composition           = Data()
        self.composition.gas       = 1.0
