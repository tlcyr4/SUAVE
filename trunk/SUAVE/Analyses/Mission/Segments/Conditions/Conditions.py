# Conditions.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# python imports
import numpy as np

# SUAVE imports
from SUAVE.Core                    import Data


# ----------------------------------------------------------------------
#  Conditions
# ----------------------------------------------------------------------

class Conditions(Data):
    """ SUAVE.Analyses.Mission.Segments.Conditions()
        Data structure for holding other Conditions and arrays of system conditions
    """
    _size = 1
    
    def ones_row(self,cols):
        """ SUAVE.Analyses.Mission.Segments.Conditions.ones_row(cols)
            returns a row vector of ones with given number of columns 
            
            Inputs:
                cols - number of columns in numpy array matrix/array
        """
        return np.ones([self._size,cols])
    
    def expand_rows(self,rows):
        """ SUAVE.Analyses.Mission.Segments.Conditions.expand_rows(cols)
            initialize size and recursively set arrays to have given length 
            
            Inputs:
                cols - number of columns in numpy array matrix/array
        """
        # store
        self._size = rows
        
        # recursively initialize condition and unknown arrays 
        # to have given row length
        
        for k,v in self.iteritems():
            # recursion
            if isinstance(v,Conditions):
                v.expand_rows(rows)
            # need arrays here
            elif np.rank(v) == 2:
                self[k] = np.resize(v,[rows,v.shape[1]])
            #: if type
        #: for each key,value
        
        return

    def compile(self):
        """ SUAVE.Analyses.Mission.Segments.Conditions.compile(cols)
            calls expand_rows 
        """
        self.expand_rows()