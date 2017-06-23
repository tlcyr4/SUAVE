# Container.py
#
# Created:  Jan 2015, T. Lukacyzk
# Modified: Feb 2016, T. MacDonald
#           Jun 2016, E. Botero


# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------        

from Data     import Data
from warnings import warn


# ----------------------------------------------------------------------
#   Data Container Base Class
# ----------------------------------------------------------------------        

class Container(Data):
    """ SUAVE.Core.Container()
        
        a dict-type container with attribute, item and index style access
        intended to hold a attribute-accessible list of Data()
        no defaults are allowed
    
    """
        
    def __defaults__(self):
        """ No defaults.
        """
        pass
    
    def __init__(self,*args,**kwarg):
        """ Initializes with defaults.
        """
        super(Container,self).__init__(*args,**kwarg)
        self.__defaults__()
    
    def append(self,val):
        """ Inherits append method from Data, adds data to the dictionary
        """
        #val = self.check_new_val(val)
        Data.append(self,val)
        
    def extend(self,vals):
        """ Simply appends vals if it is a list or tuple, recursively updates with vals if it is a dict.
        """
        if isinstance(vals,(list,tuple)):
            for v in val: self.append(v)
        elif isinstance(vals,dict):
            self.update(vals)
        else:
            raise Exception, 'unrecognized data type'
