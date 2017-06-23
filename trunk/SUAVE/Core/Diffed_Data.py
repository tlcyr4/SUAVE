# DiffedData.py
#
# Created:  Feb 2015, T. Lukacyzk
# Modified: Feb 2016, T. MacDonald
#           Jun 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from copy import deepcopy
from Container import Container as ContainerBase
from Data import Data
import numpy as np

# ----------------------------------------------------------------------
#  Config
# ----------------------------------------------------------------------

class Diffed_Data(Data):
    """ SUAVE.Core.DiffedData()
        Data object that remembers itself, a base version of itself, and the difference between the two.
    """
    
    def __defaults__(self):
        """ SUAVE.Core.Diffed_Data.__defaults__()
            Default tag is 'config' and base and diff default to default Data instances.
            
        """
        self.tag    = 'config'
        self._base  = Data()
        self._diff  = Data()
        
    def __init__(self,base=None):
        """ SUAVE.Core.Diffed_Data.__init__(base = None)
            Sets base to be the initial state and initializes as Data.
            
            Inputs:
                base - alternative base version to be stored
        """
        if base is None: base = Data()
        self._base = base
        this = deepcopy(base) # deepcopy is needed here to build configs - Feb 2016, T. MacDonald
        Data.__init__(self,this)
        
    def store_diff(self):
        """ SUAVE.Core.Diffed_Data.store_diff()
            Finds difference between itself and base and stores result.
            
        """
        delta = diff(self,self._base)
        self._diff = delta
        
    def pull_base(self):
        """ SUAVE.Core.Diffed_Data.pull_base()
            Updates with data from base.
        """
        try: self._base.pull_base()
        except AttributeError: pass
        self.update(self._base)
        self.update(self._diff)
    
    def __str__(self,indent=''):
        """ SUAVE.Core.Diffed_Data(indent = '')
            String representation includes stored difference and base.
            
            Inputs:
                indent - specifies separation between items
                
            Outputs:
                args - string representation of all data in diff and base
        """
        try: 
            args = self._diff.__str__(indent)
            args += indent + '_base : ' + self._base.__repr__() + '\n'
            args += indent + '  tag : ' + self._base.tag + '\n'
            return args
        except AttributeError:     
            return Data.__str__(self,indent)
    
    def finalize(self):
        """ SUAVE.Core.Diffed_Data.finalize()
            Updates with data from base.
        """
        ## dont do this here, breaks down stream dependencies
        # self.store_diff 
        
        self.pull_base()

# ----------------------------------------------------------------------
#  Config Container
# ----------------------------------------------------------------------

class Container(ContainerBase):
    """ SUAVE.Core.Diffed_Data.Container
        Container of Diffed Data
    """
    def append(self,value):
        """ SUAVE.Core.Diffed_Data.Container.append(value)
            Checks to see if the value is diffed data and appends.
            
            Inputs:
                value - data to be appended
        """
        try: value.store_diff()
        except AttributeError: pass
        ContainerBase.append(self,value)
        
    def pull_base(self):
        """ SUAVE.Core.Diffed_Data.Container.pull_base()
            Updates all diffed data in container with their bases
        """
        for config in self:
            try: config.pull_base()
            except AttributeError: pass

    def store_diff(self):
        """ SUAVE.Core.Diffed_Data.Container.store_diff()
            Stores differences from base for all Diffed data held in container
        """
        for config in self:
            try: config.store_diff()
            except AttributeError: pass
    
    def finalize(self):
        """ SUAVE.Core.Diffed_Data.Container.finalize()
            Updates all diffed data in container with their bases
        """
        for config in self:
            try: config.finalize()
            except AttributeError: pass


# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Diffed_Data.Container = Container

# ------------------------------------------------------------
#  Diffing Function
# ------------------------------------------------------------

def diff(A,B):
    """ SUAVE.Core.Diffed_Data.diff(A, B)
        Determines the differences between two pieces of data
        
        Inputs:
            A - a piece of data to be compared
            B - a piece of data to be compared
            
        Outputs:
            result - all key-value pairs in one pieced of data but not the other
    """

    keys = set([])
    keys.update( A.keys() )
    keys.update( B.keys() )

    if isinstance(A,Diffed_Data):
        keys.remove('_base')
        keys.remove('_diff')

    result = type(A)()
    result.clear()

    for key in keys:
        va = A.get(key,None)
        vb = B.get(key,None)
        if isinstance(va,Data) and isinstance(vb,Data):
            sub_diff = diff(va,vb)
            if sub_diff:
                result[key] = sub_diff

        elif isinstance(va,Data) or isinstance(vb,Data):
            result[key] = va

        elif not np.all(va == vb):
            result[key] = va

    return result    
