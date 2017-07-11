# Gas.py: 

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data

# ----------------------------------------------------------------------
#  Gas Data Class
# ----------------------------------------------------------------------

class Gas(Data):

    """ SUAVE.Attributes.Gases.Gas()
        Physical constants specific to a gas 
    """

    def __defaults__(self):
        """ SUAVE.Attributes.Gases.Gas.__defaults__()
            Initializes chemistry
        """
        self.molecular_mass  = 0.0    
        self.gas_specific_constant              = 0.0              
        self.composition = Data()
        self.composition.gas = 1.0
