# Unknowns.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Conditions import Conditions

# ----------------------------------------------------------------------
#  Unknowns
# ----------------------------------------------------------------------

class Unknowns(Conditions):
    """ SUAVE.Analyses.Mission.Segments.Unknowns()
        Holds unknowns (values that are varied by solver)
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Unknowns.__defaults__()
            just the tag: 'unknowns', everything else depends on what's being solved
        """
        self.tag = 'unknowns'