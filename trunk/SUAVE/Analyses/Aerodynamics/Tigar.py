# Tigar.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results
import SUAVE.Analyses.Mission.Segments.Conditions.Conditions as Conditions


# ----------------------------------------------------------------------
#   Tigar
# ----------------------------------------------------------------------   \
class Tigar(Aerodynamics):
    """ An incredibly simple and inaccurate aerodynamics model for exploring what it takes to qualify as one in SUAVE.
    """
    def evaluate(self, state):
        print state.conditions.aerodynamics
        results = Results()
        results.drag = Results()
        results.lift = Results()
        """state.conditions.aerodynamics.drag_breakdown.total = state.conditions.aerodynamics.drag_coefficient
        state.conditions.aerodynamics.drag_breakdown.parasite.total = state.conditions.aerodynamics.drag_coefficient
        state.conditions.aerodynamics.drag_breakdown.compressible = Conditions()
        #print state.conditions.aerodynamics.drag_breakdown.parasite
        state.conditions.aerodynamics.drag_breakdown.induced = Conditions()
        state.conditions.aerodynamics.drag_breakdown.induced.total = state.conditions.aerodynamics.drag_coefficient
        state.conditions.aerodynamics.drag_breakdown.compressible.total = state.conditions.aerodynamics.drag_coefficient
        state.conditions.aerodynamics.drag_breakdown.miscellaneous = Conditions()
        state.conditions.aerodynamics.drag_breakdown.miscellaneous.total = state.conditions.aerodynamics.drag_coefficient"""
        state.conditions.aerodynamics.lift_coefficient = state.conditions.aerodynamics.angle_of_attack
        state.conditions.aerodynamics.drag_coefficient = state.conditions.aerodynamics.angle_of_attack
        results.drag.total = state.conditions.aerodynamics.lift_coefficient
        
        results.lift.total = state.conditions.aerodynamics.drag_coefficient
        return results
        