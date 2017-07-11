# Composition.py
# 
# Created: Mar 2014,     J. Sinsay
# Modified: Jan, 2016,  M. Vegh



# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# initialized constants
from Constant import Constant

# exceptions/warnings
from warnings import warn

# ----------------------------------------------------------------------
#  Composition Constant Class
# ----------------------------------------------------------------------

class Composition(Constant):
    """ SUAVE.Attributes.Constants.Composition()
        Composition base class for gas mixtures 
    """
    def __defaults__(self):
        """ SUAVE.Attributes.Constants.Composition.__defaults__()
            Adds nothing to Constant defaults 
        """
        pass
    
    def __check__(self):
        """ SUAVE.Attributes.Constants.Composition.__check__()
            checks to see that the composition adds to 1.0 
        """
        # check that composition sums to 1.0
        total = 0.0
        for v in self.values():
            total += v
        other = 1.0 - total

        # set other if needed
        if other != 0.0: 
            if self.has_key('Other'):
                other += self.Other
            self.Other = other
            self.swap('Other',-1)
                
        # check for negative other
        if other < 0.0:
            warn('Composition adds to more than 1.0',Data_Warning)
