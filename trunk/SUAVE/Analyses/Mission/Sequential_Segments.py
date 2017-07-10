# Sequential_Segments.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import ContainerOrdered as ContainerBase

from SUAVE.Methods import Missions as Methods

from Mission import Mission
""" Mission.py: Top-level mission class """
# ----------------------------------------------------------------------
#   Class
# ----------------------------------------------------------------------

class Sequential_Segments(Mission):
    """ SUAVE.Analyses.Mission.Sequential_Segments()
        Solves each segment one at time 
    """
    
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Sequential_Segments.__defaults__()
            Initializes initialize, converge, iterate, and finalize processes
        """
        self.tag = 'mission'
        
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        
        # --------------------------------------------------------------
        #   Initialize
        # --------------------------------------------------------------
        self.process.initialize = Methods.Segments.Common.Sub_Segments.expand_sub_segments

        # --------------------------------------------------------------
        #   Converge
        # --------------------------------------------------------------
        self.process.converge = Methods.Segments.Common.Sub_Segments.sequential_sub_segments
        
        # --------------------------------------------------------------
        #   Iterate
        # --------------------------------------------------------------        
        del self.process.iterate

        # --------------------------------------------------------------
        #   Finalize
        # --------------------------------------------------------------        
        self.process.finalize.sub_segments = Methods.Segments.Common.Sub_Segments.finalize_sub_segments
        
        return
    
    def finalize(self):
        """ SUAVE.Analyses.Mission.Sequential_Segments.finalize()
            Does nothing
        """
        pass

# ----------------------------------------------------------------------
#   Cotnainer Class
# ----------------------------------------------------------------------

class Container(ContainerBase):
    """ SUAVE.Analyses.Mission.Sequential_Segments.Container()
        container for holding (sequential subsegment) missions
    """
    def evaluate(self,state=None):
        """ SUAVE.Analyses.Mission.Sequential_Segments.evaluate(state = None)
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
        """ SUAVE.Analyses.Mission.Sequential_Segments.finalize()
            Does nothing
        """
        pass

# Link container
Mission.Container = Container
