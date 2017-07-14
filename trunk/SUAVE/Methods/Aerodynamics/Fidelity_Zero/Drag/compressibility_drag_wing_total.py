## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
# compressibility_drag_wing_total.py
# 
# Created:  Jan 2014, SUAVE Team
# Modified: Feb 2016, T. MacDonald
#        

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
# SUAVE imports
from SUAVE.Analyses import Results
import numpy as np

# ----------------------------------------------------------------------
#  Computes the compressibility drag of the wings
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
def compressibility_drag_wing_total(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Fidelity_Zero.Drag.compressibility_drag_wing(state,settings,geometry)
        Sums compressibility drag for all wings combined
    
        Assumptions:
            None
    
        Source:
            adg.stanford.edu (Stanford AA241 A/B Course Notes)
    
        Inputs:
            state.conditions.aerodynamics.drag_breakdown.compressible[wing.tag].compressibility_drag  [Unitless]
            geometry.wings.areas.reference                                                            [m^2]
            geometry.reference_area                                                                   [m^2]
    
        Outputs:
            total_compressibility_drag                                                                [Unitless]
    
        Properties Used:
            N/A
    """ 

    # unpack
    conditions             = state.conditions
    wings                  = geometry.wings
    fuselages              = geometry.fuselages
    propulsors             = geometry.propulsors
    vehicle_reference_area = geometry.reference_area
    
    #compute parasite drag total
    total_compressibility_drag = 0.0
    
    # from wings
    for wing in wings.values():
        # scaled by reference area
        compressibility_drag = conditions.aerodynamics.drag_breakdown.compressible[wing.tag].compressibility_drag * wing.areas.reference / vehicle_reference_area
        conditions.aerodynamics.drag_breakdown.compressible[wing.tag].compressibility_drag = compressibility_drag * 1. # avoid linking variables
        total_compressibility_drag += compressibility_drag 

    conditions.aerodynamics.drag_breakdown.compressible.total  = total_compressibility_drag
        
    return total_compressibility_drag
