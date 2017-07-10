# Mission.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

""" Mission.py: Top-level mission class """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Container as ContainerBase

import Segments

# ----------------------------------------------------------------------
#   Class
# ----------------------------------------------------------------------

class Mission(Segments.Simple.Container):
    """ SUAVE.Analyses.Mission.Mission()
        Top-level mission class 
        
        Callable class, see Segments.Segment
    """
#    inherited from Segment:
#    def evaluate(self,state=None):
#        if state is None:
#            state = self.state
#        self.process(self,state)
#        return state
    
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Mission.__defaults__()
            sets tag to mission, see Segments.Simple.Container
        """
        self.tag = 'mission'
        
        # see Segments.Simple.Container
        
    def finalize(self):
        """ SUAVE.Analyses.Mission.Mission.finalize()
            mission-type-specific finalization
        """
        pass
    
    

# ----------------------------------------------------------------------
#   Container Class
# ----------------------------------------------------------------------

class Container(ContainerBase):
    """ SUAVE.Analyses.Mission.Mission.Container()
        container for holding missions
    """
    
    def evaluate(self,state=None):
        """ SUAVE.Analyses.Mission.Mission.evaluate(state = None)
            evaluates each mission in the container
            
            Inputs:
                state - optionally use predetermined state rather than missions' own
        """
        results = SUAVE.Analyses.Results()
        
        for key,mission in self.items():
            result = mission.evaluate(state)
            results[key] = result
            
        return results
    
    def finalize(self):
        """ SUAVE.Analyses.Mission.Mission.finalize()
            Does nothing
        """
        pass

# Link container
Mission.Container = Container
