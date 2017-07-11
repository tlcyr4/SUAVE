#Constant.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Core import Container as ContainerBase

# ----------------------------------------------------------------------
#  Constant Data Class
# ----------------------------------------------------------------------

class Constant(Data):
    """ SUAVE.Attributes.Constants.Constant()
        Constant Base Class, direct inheritance from Data
    """
    def __defaults__(self):
        """ SUAVE.Attributes.Constants.Constant.__defaults__()
            Adds nothing to the defaults of Data
        """
        pass

class Container(ContainerBase):
    """ SUAVE.Attributes.Constants.Constant.Container()
        Constant Container base class, direct inheritance from Container
    """
    pass

# ----------------------------------------------------------------------
#  Handle Linking
# ----------------------------------------------------------------------

Constant.Container = Container    
    
    