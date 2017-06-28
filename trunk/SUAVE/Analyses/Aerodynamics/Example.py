# Example.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results


# ----------------------------------------------------------------------
#   Example
# ----------------------------------------------------------------------   \
class Example(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Example()
        Simple and inaccurate aerodynamic model grossly approximated from a NACA 0012's lift and drag curves.
    """
    def evaluate(self, state):
        
        # Initialize results object
        results = Results()
        results.drag = Results()
        results.lift = Results()
        
        # Unpack input
        alpha = state.conditions.aerodynamics.angle_of_attack
        
        # Calculate lift and drag
        cl = 1.25 / 12 * alpha
        cd = alpha ** 2 + 0.1
        
        # Correct for stall
        # Note: inputs and outputs are numpy arrays
        for index in range(len(alpha)):
            if alpha[index] > 12.:
                cl[index] = 2 - .25/3 * alpha
                
        # Pack up results
        results.drag.total = cd
        results.lift.total = cl
        
        return results
        
