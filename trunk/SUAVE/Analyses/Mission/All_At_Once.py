# All_At_Once.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

""" All_At_Once: Solves all segments and sub segments at once """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Methods import Missions as Methods

from Mission import Mission

# ----------------------------------------------------------------------
#   Class
# ----------------------------------------------------------------------

class All_At_Once(Mission):
    """ SUAVE.Analyses.Mission.All_At_Once()
        Solves all segments and sub segments at once 
    """
    
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.All_At_Once.__defaults__()
            Initializes initialize, converge, iterate, and finalize processes
        """
        self.tag = 'mission'
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        
        # --------------------------------------------------------------
        #   Initialize
        # --------------------------------------------------------------
        self.process.initialize.expand_state        = Methods.Segments.expand_state
        self.process.initialize.expand_sub_segments = Methods.Segments.Common.Sub_Segments.expand_sub_segments

        # --------------------------------------------------------------
        #   Converge
        # --------------------------------------------------------------
        self.process.converge.converge_root         = Methods.Segments.converge_root
        
        # --------------------------------------------------------------
        #   Iterate
        # --------------------------------------------------------------        
        self.process.iterate.sub_segments           = Methods.Segments.Common.Sub_Segments.update_sub_segments

        # --------------------------------------------------------------
        #   Finalize
        # --------------------------------------------------------------        
        self.process.finalize.sub_segments          = Methods.Segments.Common.Sub_Segments.finalize_sub_segments
        
    def finalize(self):
        """ SUAVE.Analyses.Mission.All_At_Once.finalize()
            Does nothing
        """
        pass
    
    