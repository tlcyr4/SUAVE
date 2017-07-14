# __init__.py
# 
# Created:  Aug 2014, E. Botero
# Modified: Feb 2016, T. MacDonald

# ------------------------------------------------------------
#  Imports
# ------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Components import Physical_Component

# ----------------------------------------------------------------------
#  Energy Component Class
# ----------------------------------------------------------------------

class Energy_Component(Physical_Component):
    """ SUAVE.Components.Energy.Energy_Component()
        Component of energy network
    """
    def __defaults__(self):
        """ SUAVE.Components.Energy.Energy_Component.__defaults__()
            Initializes inputs and outputs to component
        """
        # function handles for input
        self.inputs  = Data()
        
        # function handles for output
        self.outputs = Data()
        
        return