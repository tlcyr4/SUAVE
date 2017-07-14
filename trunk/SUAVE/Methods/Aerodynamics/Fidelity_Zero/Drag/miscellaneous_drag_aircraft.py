## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
# miscellaneous_drag_aircraft.py
# 
# Created:  Dec 2013, SUAVE Team
# Modified: Jan 2016, E. Botero       

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
from SUAVE.Analyses import Results

# package imports
import numpy as np

# ----------------------------------------------------------------------
#  Miscellaneous Drag Aircraft
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
def miscellaneous_drag_aircraft(conditions,configuration,geometry):
    """ SUAVE.Methods.Aerodynamics.Fidelity_Zero.Drag.miscellaneous_drag_aircraft(conditions,configuration,geometry)
        Computes the miscellaneous drag associated with an aircraft
    
        Assumptions:
            Basic fit
    
        Source:
            adg.stanford.edu (Stanford AA241 A/B Course Notes)
    
        Inputs:
            configuration.trim_drag_correction_factor  [Unitless]
            geometry.propulsors.nacelle_diameter       [m]
            geometry.reference_area                    [m^2]
            geometry.wings['main_wing'].aspect_ratio   [Unitless]
            state.conditions.freestream.mach_number    [Unitless] (actual values are not used)
    
        Outputs:
            total_miscellaneous_drag                   [Unitless]
    
        Properties Used:
            N/A
    """

    # unpack inputs
    trim_correction_factor = configuration.trim_drag_correction_factor    
    propulsors             = geometry.propulsors
    vehicle_reference_area = geometry.reference_area
    ones_1col              = conditions.freestream.mach_number *0.+1
        
    # ------------------------------------------------------------------
    #   Control surface gap drag
    # ------------------------------------------------------------------
    #f_gaps_w=0.0002*(numpy.cos(sweep_w))**2*S_affected_w
    #f_gaps_h=0.0002*(numpy.cos(sweep_h))**2*S_affected_h
    #f_gaps_v=0.0002*(numpy.cos(sweep_v))**2*S_affected_v

    #f_gapst = f_gaps_w + f_gaps_h + f_gaps_v
    
    # TODO: do this correctly
    total_gap_drag = 0.0001

    # ------------------------------------------------------------------
    #   Nacelle base drag
    # ------------------------------------------------------------------
    total_nacelle_base_drag = 0.0
    nacelle_base_drag_results = Results()
    
    for propulsor in propulsors.values():
        
        # calculate
        nacelle_base_drag = 0.5/12. * np.pi * propulsor.nacelle_diameter * 0.2/vehicle_reference_area
        
        # dump
        nacelle_base_drag_results[propulsor.tag] = nacelle_base_drag * ones_1col
        
        # increment
        total_nacelle_base_drag += nacelle_base_drag
        

    # ------------------------------------------------------------------
    #   Fuselage upsweep drag
    # ------------------------------------------------------------------
    fuselage_upsweep_drag = 0.006 / vehicle_reference_area
    
    # ------------------------------------------------------------------
    #   Fuselage base drag
    # ------------------------------------------------------------------    
    fuselage_base_drag = 0.0
    
    # ------------------------------------------------------------------
    #   The final result
    # ------------------------------------------------------------------
    
    total_miscellaneous_drag = total_gap_drag          \
                             + total_nacelle_base_drag \
                             + fuselage_upsweep_drag   \
                             + fuselage_base_drag 
    
    
    # dump to results
    conditions.aerodynamics.drag_breakdown.miscellaneous = Results(
        fuselage_upsweep = fuselage_upsweep_drag     *ones_1col, 
        nacelle_base     = nacelle_base_drag_results ,
        fuselage_base    = fuselage_base_drag        *ones_1col,
        control_gaps     = total_gap_drag            *ones_1col,
        total            = total_miscellaneous_drag  *ones_1col,
    )
       
    return total_miscellaneous_drag *ones_1col
    
