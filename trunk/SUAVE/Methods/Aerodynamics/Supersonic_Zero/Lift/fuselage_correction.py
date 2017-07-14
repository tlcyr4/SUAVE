# compute_aircraft_lift.py
# Created:  Dec 2013, A. Variyar 
# Modified: Feb 2014, A. Variyar, T. Lukaczyk, T. Orra 
#           Apr 2014, A. Variyar
#           Aug 2014, T. Macdonald
#           Jan 2015, E. Botero
# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Analyses import Results

# ----------------------------------------------------------------------
#  Fuselage Correction
# ----------------------------------------------------------------------

def fuselage_correction(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Supersonic_Zero.Lift.fuselage_correction(state,settings,geometry)
        applier fuselage lift correction
        
        Inputs:
            state.conditions. - data dictionary with fields:
                freestream.
                    mach_number - float or 1D array of freestream mach numbers
                aerodynamics.
                    angle_of_attack - floar or 1D array of angle of attacks
                
            settings - data dictionary with fields:
                fuselage_lift_correction - the correction to fuselage contribution to lift
                    
            geometry - used for wing
            
        
        Outputs:
            aircraft_lift_total - float or 1D array of lift coefficients of the total aircraft
        
        Updates:
            state.conditions.aerodynamics.lift_coefficient - stores results here
        
    """   
    # unpack
    fus_correction  = settings.fuselage_lift_correction
    Mc              = state.conditions.freestream.mach_number
    AoA             = state.conditions.aerodynamics.angle_of_attack
    
    wings_lift_comp = state.conditions.aerodynamics.lift_coefficient

   
    # total lift, accounting one fuselage
    aircraft_lift_total = wings_lift_comp * fus_correction
    
    # store results
    lift_results = Results(
        total                = aircraft_lift_total ,
        compressible_wings   = wings_lift_comp     ,
    )
    
    state.conditions.aerodynamics.lift_coefficient= aircraft_lift_total

    return aircraft_lift_total