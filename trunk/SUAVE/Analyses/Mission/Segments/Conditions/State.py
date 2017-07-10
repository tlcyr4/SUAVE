# State.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# python imports
import numpy as np

# SUAVE imports
from Conditions import Conditions
from Unknowns   import Unknowns
from Residuals  import Residuals
from Numerics   import Numerics

import SUAVE
from SUAVE.Core.Arrays import array_type
from SUAVE.Core import DataOrdered

# ----------------------------------------------------------------------
#  State
# ----------------------------------------------------------------------

class State(Conditions):
    """ SUAVE.Analyses.Mission.Segments.State()
        Encapsulates state of a physical system and its analysis.  Holds all the information necessary to carry out analyses.
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.State.__defaults__()
            initializes unknowns, conditions, residuals, numerics, initials
        """
        
        self.unknowns   = Unknowns()
        
        self.conditions = Conditions()
        
        self.residuals  = Residuals()
        
        self.numerics   = Numerics()
        
        self.initials   = Conditions()
        
        
    def expand_rows(self,rows):
        """ SUAVE.Analyses.Mission.Segments.State.expand_rows()
            recursively expands the arrays of conditions to have a given number of rows except for initials and numerics
        """
        # store
        self._size = rows
        
        for k,v in self.iteritems():
            
            # don't expand initials or numerics
            if k in ('initials','numerics'):
                continue
            
            # recursion
            elif isinstance(v,Conditions):
                v.expand_rows(rows)
            # need arrays here
            elif np.rank(v) == 2:
                self[k] = np.resize(v,[rows,v.shape[1]])
            #: if type
        #: for each key,value        
        
        
        
class Container(State):
    """ SUAVE.Analyses.Mission.Segments.State.Container()
        Container of states
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.State.Container.__defaults__()
            just initializes DataOrdered object to hold segments
        """
        self.segments = DataOrdered()
        
    def merged(self):
        """ SUAVE.Analyses.Mission.Segments.State.Container.merged()
            Merges all states in container into one state, stacking conditions vertically
        """
        state_out = State()
        
        for i,(tag,sub_state) in enumerate(self.segments.items()):
            for key in ['unknowns','conditions','residuals']:
                if i == 0:
                    state_out[key].update(sub_state[key])
                else:
                    state_out[key] = state_out[key].do_recursive(append_array,sub_state[key])
            
        return state_out
        
State.Container = Container


def append_array(A,B=None):
    """ SUAVE.Analyses.Mission.Segments.State.append_array()
        Stack arrays vertically into one
    """
    if isinstance(A,array_type) and isinstance(B,array_type):
        return np.vstack([A,B])
    else:
        return None