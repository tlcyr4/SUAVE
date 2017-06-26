# Tigar.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results
import SUAVE.Analyses.Process as Process
import SUAVE.Methods.Aerodynamics.Example as Methods


# ----------------------------------------------------------------------
#   Tigar
# ----------------------------------------------------------------------   \
class Structured_Example(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Tigar()
        Simple and inaccurate aerodynamic model grossly approximated from a NACA 0012's lift and drag curves.
    """
    def evaluate(self, state):
        
        # set up processes
        self.process = Process()
        self.process.compute = Process()
        self.process.compute.lift = Process()
        self.process.compute.lift.total = Methods.example_lift
        self.process.compute.drag = Process()
        self.process.compute.drag.total = Methods.example_drag
        # evaluate
        results = self.process.compute(self, state)
        
        return results
        