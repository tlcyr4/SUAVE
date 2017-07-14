# Results.py
# 
# Created:  Jan 2015, T. Momose
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
from SUAVE.Core import Data

# ------------------------------------------------------------
#   Wing
# ------------------------------------------------------------

class Results(Data):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Results()
        Results data structure for handling AVL output: aerodynamics and stability
    """
    def __defaults__(self):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Results.__defaults__()
            Initializes aerodynamics and stability data structures
        """

        self.aerodynamics = Data()
        self.stability    = Data()

        self.stability.alpha_derivatives = Data()
        self.stability.beta_derivatives  = Data()