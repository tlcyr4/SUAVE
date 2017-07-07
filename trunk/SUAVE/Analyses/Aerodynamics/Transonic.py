# Transonic.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results
import numpy as np
import Fidelity_Zero
import Supersonic_Zero
    
# ----------------------------------------------------------------------
#   Example
# ----------------------------------------------------------------------   \
class Transonic(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Transonic()
        Model based on NASA CRM Transonic Experimental Data (curve fits)
    """
    
    def __defaults__(self):
        """ SUAVE.Analyses.Aerodynamics.Transonic.__defaults__()
            initializes non-transonic models
        """
        # initialize subsonic model
        model = Fidelity_Zero.Fidelity_Zero()
        model.geometry = self.geometry    
        model.process.compute.lift.inviscid_wings.geometry = self.geometry
        model.process.compute.lift.inviscid_wings.initialize()
        self.fzero = model
        
        # initialize supersonic model
        model = Supersonic_Zero.Supersonic_Zero()
        model.geometry = self.geometry
        model.process.compute.lift.inviscid_wings.geometry = self.geometry
        model.process.compute.lift.inviscid_wings.initialize()
        self.szero = Supersonic_Zero.Supersonic_Zero()
        
    
    
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
        
        
        mean = np.mean(mach)
        # Subsonic model
        if mean < .8:
            results = self.fzero(state)

        # Supersonic model
        elif mean > 1.2:
            results = self.szero(state)
            
        else:
            
            cl, cd = tandem(alpha)
            
            results.lift.total = cl
            results.drag.total = cd
            
        return results
    
def quadratic_single(aoa):
    """ SUAVE.Analyses.Aerodynamics.Transonic.tandem(aoa)
        Uses aoa to calculate cl and cd with quadratic curve fits
        
        Inputs:
            aoa - angle of attack (column array)
            
        Outputs:
            cl - lift coefficient (column array)
            cd - drag coefficient (column array)
    """
    # model coefficients
    bl = np.array([[-0.00717433179381432],	[0.144047701950893],	[0.126479444126983]])
    bd = np.array([[0.00162236444781382],	[0.000443156656073951],	[0.0141465405789619]])
    
    # calculate coefficients
    cl = bl[2] + bl[1] * aoa + bl[0] * np.square(aoa)
    cd = bd[2] + bd[1] * aoa + bd[0] * np.square(aoa)
    
    return cl, cd

def tandem(aoa):
    """ SUAVE.Analyses.Aerodynamics.Transonic.tandem(aoa)
        Uses aoa to calculate cl and cl to calculate cd
        
        Inputs:
            aoa - angle of attack (column array)
            
        Outputs:
            cl - lift coefficient (column array)
            cd - drag coefficient (column array)
    """
    # model coefficients
    bl = np.array([[-0.00717433179381432],	[0.144047701950893],	[0.126479444126983]])
    bd = np.array([[0.177990108978307],	[0.04257289502394],	[0.010275150311500]])
    
    # calculate coefficients
    cl = bl[2] + bl[1] * aoa + bl[0] * np.square(aoa)
    cd = bd[2] + bd[1] * cl + bd[0] * np.square(cl)
    
    return cl, cd
# ----------------------------------------------------------------------
#   Module Testing
# ----------------------------------------------------------------------   
def main():
    import SUAVE.Analyses.Mission.Segments.Conditions.State as State
    import SUAVE.Analyses.Mission.Segments.Conditions.Aerodynamics as Aerodynamics

    state = State()
    state.conditions.update(Aerodynamics())

    state.conditions.freestream.mach_number = np.array([[.8503]])
    state.conditions.aerodynamics.angle_of_attack = np.array([[4]])
    state.conditions.aerodynamics.side_slip_angle = np.array([[0.0353]])
    state.conditions.aerodynamics.roll_angle = np.array([[180.0]])
    
    transonic = Transonic()
#    result = transonic.evaluate(state)
#    print result.drag.total
#    print result.lift.total
#    print transonic.settings.maximum_lift_coefficient
    
#    model = Fidelity_Zero.Fidelity_Zero()
#    model.settings = trans.settings
#    model.geometry = trans.geometry
#    
#    model.process.compute.lift.inviscid_wings.geometry = trans.geometry
#    model.process.compute.lift.inviscid_wings.initialize()
#    
#    print model.process.compute.lift.inviscid_wings

main()

