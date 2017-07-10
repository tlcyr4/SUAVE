# Segment.py
#
# Created:  
# Modified: Sep 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports

from SUAVE.Analyses import Analysis, Settings, Process
from Conditions import State

# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Segment(Analysis):
    """ SUAVE.Analyses.Mission.Segments.Segment()
        Base class for mission segments, a discrete part of a mission
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Segment.__defaults__()
            initializes initialize, converge, iterate, and finalize processes
        """
        self.settings = Settings()
        
        self.state = State()

        self.analyses = Analysis.Container()
        
        self.process = Process()
        self.process.initialize            = Process()
        self.process.converge              = Process()
        self.process.iterate               = Process()
        self.process.iterate.unknowns      = Process()
        self.process.iterate.initials      = Process()
        self.process.iterate.conditions    = Process()
        self.process.iterate.residuals     = Process()
        self.process.finalize              = Process()
        self.process.finalize.post_process = Process()
        
        return
        

    def initialize(self,state):
        """ SUAVE.Analyses.Mission.Segments.Segment.initialize()
            initializes segment
        """
        self.process.initialize(self,state)
        return
    
    def converge(self,state):
        """ SUAVE.Analyses.Mission.Segments.Segment.converge()
            starts iteration process and attempts to converge residuals to 0
            
            Inputs:
                state - state of the system
        """
        self.process.converge(self,state)    
    
    def iterate(self,state):
        """ SUAVE.Analyses.Mission.Segments.Segment.iterate()
            runs one iteration, updating all values
            
            Inputs:
                state - state of the system
        """
        self.process.iterate(self,state)
        return
    
    def finalize(self,state):
        """ SUAVE.Analyses.Mission.Segments.Segment.finalize()
            any post processing after segment converges
            
            Inputs:
                state - state of the system
        """
        self.process.finalize(self,state)
        return
 
    def compile(self):
        return
    
                        
    def evaluate(self,state=None):
        """ SUAVE.Analyses.Mission.Segments.Segment.iterate()
            runs one iteration, updating all values
            
            Inputs:
                state - state of the system
        """
        if state is None:
            state = self.state
        self.process(self,state)
        return state
    
    
# ----------------------------------------------------------------------
#  Container
# ----------------------------------------------------------------------

class Container(Segment):
    """ SUAVE.Analyses.Mission.Segments.Segment.Container()
            Container for holding segments
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Segment.Container.__defaults__()
            initializes segments process and default state
        """
                
        self.segments = Process()
        
        self.state = State.Container()
        
    def append_segment(self,segment):
        """ SUAVE.Analyses.Mission.Segments.Segment.Container.append_segment()
            Adds a subsegment
            
            Inputs:
                segment - segment to be added
        """
        self.segments.append(segment)
        return    
        
Segment.Container = Container