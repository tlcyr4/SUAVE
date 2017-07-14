## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
# parasite_drag_pylon.py
# 
# Created:  Jan 2014, T. Orra
# Modified: Jan 2016, E. Botero   

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
import numpy as np

# Suave imports
from SUAVE.Analyses import Results

# ----------------------------------------------------------------------
#  Computes the pyloan parasite drag
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
def parasite_drag_pylon(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Fidelity_ZeroDrag..parasite_drag_pylon(state,settings,geometry)
        Computes the parasite drag due to pylons as a proportion of the propulsor drag
    
        Assumptions:
            Basic fit
    
        Source:
            adg.stanford.edu (Stanford AA241 A/B Course Notes)
    
        Inputs:
            conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].
              form_factor                                                   [Unitless]
              compressibility_factor                                        [Unitless]
              skin_friction_coefficient                                     [Unitless]
              wetted_area                                                   [m^2]
              parasite_drag_coefficient                                     [Unitless]
              reynolds_number                                               [Unitless]
            geometry.reference_area                                         [m^2]
            geometry.propulsors. 
              nacelle_diameter                                              [m]
              number_of_engines                                             [Unitless]
    
        Outputs:
            propulsor_parasite_drag                                         [Unitless]
    
        Properties Used:
            N/A
    """
    # unpack
    
    conditions = state.conditions
    configuration = settings
    
    pylon_factor        =  0.20 # 20% of propulsor drag
    n_propulsors        =  len(geometry.propulsors)  # number of propulsive system in vehicle (NOT # of ENGINES)
    pylon_parasite_drag = 0.00
    pylon_wetted_area   = 0.00
    pylon_cf            = 0.00
    pylon_compr_fact    = 0.00
    pylon_rey_fact      = 0.00
    pylon_FF            = 0.00

    # Estimating pylon drag
    for propulsor in geometry.propulsors:
        ref_area = propulsor.nacelle_diameter**2 / 4 * np.pi
        pylon_parasite_drag += pylon_factor *  conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].parasite_drag_coefficient* (ref_area/geometry.reference_area * propulsor.number_of_engines)
        pylon_wetted_area   += pylon_factor *  conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].wetted_area * propulsor.number_of_engines
        pylon_cf            += conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].skin_friction_coefficient
        pylon_compr_fact    += conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].compressibility_factor
        pylon_rey_fact      += conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].reynolds_factor
        pylon_FF            += conditions.aerodynamics.drag_breakdown.parasite[propulsor.tag].form_factor
        
    pylon_cf            /= n_propulsors           
    pylon_compr_fact    /= n_propulsors   
    pylon_rey_fact      /= n_propulsors     
    pylon_FF            /= n_propulsors      
    
    # dump data to conditions
    pylon_result = Results(
        wetted_area               = pylon_wetted_area   ,
        reference_area            = geometry.reference_area   ,
        parasite_drag_coefficient = pylon_parasite_drag ,
        skin_friction_coefficient = pylon_cf  ,
        compressibility_factor    = pylon_compr_fact   ,
        reynolds_factor           = pylon_rey_fact   ,
        form_factor               = pylon_FF   ,
    )
    conditions.aerodynamics.drag_breakdown.parasite['pylon'] = pylon_result 
 
    return pylon_parasite_drag