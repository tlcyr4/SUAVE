# Analysis.py
# 
# Created:  Unk,     , T. Lukaczyk
# Modified: Jan, 2016, M. Vegh



# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data

# ----------------------------------------------------------------------
#  Analysis Data Class
# ----------------------------------------------------------------------

class Analysis(Data):
    """ \deprecated
        SUAVE.Attributes.Analysis()
        SUAVE Data Class for Analysis
        used for carrying out analyses
    """
    def __defaults__(self):
        """ \deprecated
            SUAVE.Attributes.Analysis.__defaults__()
            Initializes vehicle, mission, and procedure (old version of process)
        """
        self.Vehicle = None
        self.Mission = None
        self.Procedure = AnalysisMap()
        
    def solve(self):
        """ \deprecated
            SUAVE.Attributes.Analysis.solve()
            solves all procedures
        """
        procedure = self.procedure
        for segment,configuration in procedure.items():
            results = segment.solve(configuration)
        
    def __str__(self):
        """ \deprecated
            SUAVE.Attributes.Analysis.__str__()
            String representation includes dataname, vehicle, mission, procedure, and subprocedures
        """
        args = ''
        args += self.dataname() + '\n'
        args += 'Vehicle = %s\n' % self.Vehicle.tag
        args += 'Mission = %s\n' % self.Mission.tag
        args += 'Procedure =\n'
        for step in self.Procedure.values():
            seg = step[0]
            con = step[1]
            args += '  %s : %s\n' % (seg.tag,con.tag)
        return args
        
class AnalysisMap(Data):
    """ \deprecated
        SUAVE.Attributes.Analysis.AnalysisMap()
        Unimplemented
    """
    pass