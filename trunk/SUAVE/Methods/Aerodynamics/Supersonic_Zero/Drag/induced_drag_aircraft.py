## @ingroup methods-aerodynamics-Supersonic_Zero-Drag
# induced_drag_aircraft.py
# 
# Created:  Aug 2014, T. MacDonald
# Modified: Nov 2016, T. MacDonald
     
# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Analyses import Results

import numpy as np

# ----------------------------------------------------------------------
#  Induced Drag Aicraft
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Supersonic_Zero-Drag
def induced_drag_aircraft(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Supersonic_Zero.Drag.induced_drag_aircraft(state,settings,geometry)
        Determines induced drag for the full aircraft
    
        Assumptions:
            Based on fits
    
        Source:
            adg.stanford.edu (Stanford AA241 A/B Course Notes)
    
        Inputs:
            state.conditions.aerodynamics.lift_coefficient               [Unitless]
            state.conditions.aerodynamics.drag_breakdown.parasite.total  [Unitless]
            configuration.oswald_efficiency_factor                       [Unitless]
            configuration.viscous_lift_dependent_drag_factor             [Unitless]
            geometry.wings['main_wing'].span_efficiency                  [Unitless]
            geometry.wings['main_wing'].aspect_ratio                     [Unitless]
    
        Outputs:
            total_induced_drag                                           [Unitless]
    
        Properties Used:
            N/A
    """

    # unpack inputs
    conditions = state.conditions
    configuration = settings    
    
    aircraft_lift = conditions.aerodynamics.lift_coefficient
    
    e             = configuration.oswald_efficiency_factor
    K             = configuration.viscous_lift_dependent_drag_factor
    wing_e        = geometry.wings['main_wing'].span_efficiency
    ar            = geometry.wings['main_wing'].aspect_ratio 
    CDp           = state.conditions.aerodynamics.drag_breakdown.parasite.total
    
    if e == None:
        e = 1/((1/wing_e)+np.pi*ar*K*CDp)    
    
    total_induced_drag = aircraft_lift**2 / (np.pi*ar*e)
        
    # store data
    try:
        conditions.aerodynamics.drag_breakdown.induced = Results(
            total             = total_induced_drag ,
            efficiency_factor = e                  ,
            aspect_ratio      = ar                 ,
        )
    except:
        print("Drag Polar Mode")     
    
    return total_induced_drag