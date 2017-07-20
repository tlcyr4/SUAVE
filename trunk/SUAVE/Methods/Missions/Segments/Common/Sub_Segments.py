# Sub_Segments.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero
#           Mar 2016, E. Botero

from copy import deepcopy

# ----------------------------------------------------------------------
#  Expand Sub Segments
# ----------------------------------------------------------------------
          
def expand_sub_segments(segment,state):
    """ SUAVE.Methods.Missions.Segments.Common.Sub_Segments.expand_sub_segments(segment,state)
        initialize subsegments and expand their conditions

        Inputs:
            segment.items

        Outputs:
            See Updates

        Updates:
            state.
                segments
                unknowns
                conditions
                residuals
    """
    from SUAVE.Analyses import Process
    
    last_tag = None
    
    for tag,sub_segment in segment.segments.items():
        
        if Process.verbose:
            print 'segment start :' , tag
        
        sub_state = deepcopy( sub_segment.state )
        
        if last_tag:
            sub_state.initials = state.segments[last_tag]
        last_tag = tag        
        
        sub_segment.initialize(sub_state)
        
        state.segments[tag]     = sub_state
        state.unknowns[tag]     = sub_state.unknowns
        state.conditions[tag]   = sub_state.conditions
        state.residuals[tag]    = sub_state.residuals
        
        if Process.verbose:
            print 'segment end :' , tag        


# ----------------------------------------------------------------------
#  Update Sub Segments
# ----------------------------------------------------------------------        

def update_sub_segments(segment,state):
    """ SUAVE.Methods.Missions.Segments.Common.Sub_Segments.update_sub_segments(segment,state)
        update subsegments and their conditions

        Inputs:
            segments.items

        Outputs:
            See Updates

        Updates:
            calls initialize, iterate. and finalize on each subsegment
    """
    for tag,sub_segment in segment.segments.items():
        sub_segment.initialize(state.segments[tag])
        sub_segment.iterate(state.segments[tag])
        sub_segment.finalize(state.segments[tag])
                         
# ----------------------------------------------------------------------
#  Finalize Sub Segments
# ----------------------------------------------------------------------

def finalize_sub_segments(segment,state):
    """ SUAVE.Methods.Missions.Segments.Common.Sub_Segments.finalize_sub_segments(segment,state)
        postprocessing on subsegments

        Inputs:
            segment.items

        Outputs:
            See Updates

        Updates:
            each segment calls finalize
    """
    from SUAVE.Analyses.Mission.Segments.Conditions import Conditions
    
    for tag,sub_segment in segment.segments.items():
        sub_segment.finalize(state.segments[tag])
        state.segments[tag].initials = Conditions()

# ----------------------------------------------------------------------
#  Sequential Sub Segments
# ----------------------------------------------------------------------

def sequential_sub_segments(segment,state):
    """ SUAVE.Methods.Missions.Segments.Common.Sub_Segments.expand_sub_segments(segment,state)
        initialize subsegments and expand their conditions

        Inputs:
            segment.items

        Outputs:
            See Updates

        Updates:
            each segment calls evaluate
    """
    for tag,sub_segment in segment.segments.items():
        sub_segment.evaluate(state.segments[tag])