## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
# miscellaneous_drag_aircraft_ESDU.py
# 
# Created:  Jan 2014, T. Orra
# Modified: Jan 2016, E. Botero    

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
# SUAVE imports
from SUAVE.Analyses import Results

# ----------------------------------------------------------------------
#  Computes the miscellaneous drag
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Fidelity_Zero-Drag
def miscellaneous_drag_aircraft_ESDU(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Fidelity_Zero.Drag.miscellaneous_drag_aircraft_ESDU(state,settings,geometry)
        Computes the miscellaneous drag associated with an aircraft
    
        Assumptions:
            Basic fit
    
        Source:
            ESDU 94044, figure 1
    
        Inputs:
            state.conditions.freestream.mach_number    [Unitless] (actual values not used)
            geometry.reference_area                    [m^2]
            geometry.wings.areas.wetted                [m^2]
            geometry.fuselages.areas.wetted            [m^2]
            geometry.propulsor.areas.wetted            [m^2]
            geometry.propulsor.number_of_engines       [Unitless]
    
        Outputs:
            cd_excrescence (drag)                      [Unitless]
    
        Properties Used:
            N/A
    """

    # unpack inputs
    
    conditions    = state.conditions
    configuration = settings
    
    Sref      = geometry.reference_area
    ones_1col = conditions.freestream.mach_number *0.+1

    # Estimating total wetted area
    swet_tot        = 0.
    for wing in geometry.wings:
        swet_tot += wing.areas.wetted

    for fuselage in geometry.fuselages:
        swet_tot += fuselage.areas.wetted

    for propulsor in geometry.propulsors:
        swet_tot += propulsor.areas.wetted * propulsor.number_of_engines

    swet_tot *= 1.10
    
    # Estimating excrescence drag, based in ESDU 94044, figure 1
    D_q = 0.40* (0.0184 + 0.000469 * swet_tot - 1.13*10**-7 * swet_tot ** 2)
    cd_excrescence = D_q / Sref

    # ------------------------------------------------------------------
    #   The final result
    # ------------------------------------------------------------------
    # dump to results
    conditions.aerodynamics.drag_breakdown.miscellaneous = Results(
        total_wetted_area         = swet_tot,
        reference_area            = Sref ,
        total                     = cd_excrescence *ones_1col, )

    return cd_excrescence *ones_1col
