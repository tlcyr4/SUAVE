# Transonic.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: Jul 2017, Tigar Cyr

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results
from SUAVE.Methods.Aerodynamics import Transonic as Methods
import numpy as np
import warnings
    
# ----------------------------------------------------------------------
#   Transonic
# ----------------------------------------------------------------------
class Transonic(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Transonic()
        Model based on NASA CRM Transonic Experimental Data (curve fits)
    """

    def evaluate(self, state):
        """ SUAVE.Analyses.Aerodynamics.evaluate(state)
            evaluate aerodynamic analysis
            
            Inputs:
                state.conditions.freestream.mach_number - mach number (column array)
                state.conditions.aerodynamics.angle_of_attack - aoa (column array)
                
            Outputs:
                results.lift.total - lift coefficient (column array)
                results.drag.total - drag coefficient (column array)
        """
        
        # Initialize results object
        results = Results()
        results.drag = Results()
        results.lift = Results()
        
        # Unpack input
        mach = state.conditions.freestream.mach_number
        alpha = state.conditions.aerodynamics.angle_of_attack
        
        alphamax = 8
        alphamin = -3
        
        alpha[alpha > alphamax] = alphamax
        alpha[alpha < alphamin] = alphamin
        
        
        mean = np.mean(mach)
        # Check to see if model is transonic
        if mean < .8:
            warnings.warn("System is subsonic. Consider using different model")
        elif mean > 1.2:
            warnings.warn("System is supersonic. Consider using different model")

            
        cl = Methods.compute_lift(alpha)
        
        results.lift.total = cl
        cd = Methods.compute_drag_from_lift(cl)
        results.drag.total = cd
        
        state.conditions.aerodynamics.lift_coefficient = cl
        state.conditions.aerodynamics.drag_coefficiemt = cd
            
        return results
    



# ----------------------------------------------------------------------
#   Module Testing
# ----------------------------------------------------------------------   
def main():
    import SUAVE.Analyses.Mission.Segments.Conditions.State as State
    import SUAVE.Analyses.Mission.Segments.Conditions.Aerodynamics as Aerodynamics

    state = State()
    state.conditions.update(Aerodynamics())

    state.conditions.freestream.mach_number = np.array([[.8503],[.85],[.85]])
    state.conditions.aerodynamics.angle_of_attack = np.array([[0],[1],[2]])
    state.conditions.aerodynamics.side_slip_angle = np.array([[0],[0],[0]])
    state.conditions.aerodynamics.roll_angle = np.array([[180.0],[180],[180]])
    
    transonic = Transonic()
    result = transonic.evaluate(state)
    print result.drag.total
    print result.lift.total
    print transonic.settings.maximum_lift_coefficient
    
#    model = Fidelity_Zero.Fidelity_Zero()
#    model.settings = trans.settings
#    model.geometry = trans.geometry
#    
#    model.process.compute.lift.inviscid_wings.geometry = trans.geometry
#    model.process.compute.lift.inviscid_wings.initialize()
#    
#    print model.process.compute.lift.inviscid_wings

if __name__ == '__main__':
    main()

