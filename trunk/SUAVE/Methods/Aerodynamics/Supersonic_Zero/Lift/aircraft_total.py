# compute_aircraft_lift.py
# 
# Created:  Dec 2013, A. Variyar,
# Modified: Feb 2014, A. Variyar, T. Lukaczyk, T. Orra 
#           Apr 2014, A. Variyar  
#           Aug 2014, T. Macdonald
#           Jan 2016, E. Botero       

# ----------------------------------------------------------------------
#  Aircraft Total
# ----------------------------------------------------------------------

def aircraft_total(state,settings,geometry):
    """ SUAVE.Methods.Aerodynamics.Supersonic_Zero.Lift.aircraft_lift_total(conditions,configuration,geometry)
        computes the lift associated with an aircraft 
        
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
    fus_correction = settings.fuselage_lift_correction
    Mc             = state.conditions.freestream.mach_number
    AoA            = state.conditions.aerodynamics.angle_of_attack
    
    aircraft_lift_total = state.conditions.aerodynamics.lift_coefficient
    state.conditions.aerodynamics.lift_coefficient = aircraft_lift_total    

    return aircraft_lift_total