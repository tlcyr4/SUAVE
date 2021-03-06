# ContainerOrdered.py
#
# Created:  Jan 2015, T. Lukacyzk
# Modified: Feb 2016, T. MacDonald
#           Jun 2016, E. Botero


# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------        

from DataOrdered import DataOrdered
from warnings    import warn

# ----------------------------------------------------------------------
#   Data Container Base Class
# ----------------------------------------------------------------------        

class ContainerOrdered(DataOrdered):
    """ SUAVE.Core.ContainerOrdered()
        
        OrderedDict-type container with attribute-style access.
    
    """
        
    def __defaults__(self):
        """ SUAVE.Core.ContainerOrdered.__defaults__()
            No defaults to add.
        """
        pass
    
    def __init__(self,*args,**kwarg):
        """ SUAVE.Core.ContainerOrdered.__init__(*args, **kwargs)
            Initializes with defaults.
            
            Inputs:
                *args - input data to be appended into data object
                **kwarg - input data to be appended into data object
        """
        super(ContainerOrdered,self).__init__(*args,**kwarg)
        self.__defaults__()
    
    def append(self,val):
        """ SUAVE.Core.ContainerOrdered.append(val)
            Add an entry to the dictionary with tag as key.
            
            Inputs:
                value - value to be added
        """
        #val = self.check_new_val(val)
        DataOrdered.append(self,val)
        
    def extend(self,vals):
        """ SUAVE.Core.ContainerOrdered.extend(vals)
            Adds values to container. Appends for list/tuple, updates for dict.
            
            Inputs:
                vals - values to be added to container
        """
        if isinstance(vals,(list,tuple)):
            for v in val: self.append(v)
        elif isinstance(vals,dict):
            self.update(vals)
        else:
            raise Exception, 'unrecognized data type'
