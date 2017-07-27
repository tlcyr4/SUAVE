# turbofan_nox_emission_index.py
# 
# Created:  Sep 2015, M. Vegh
# Modified: Feb 2016, E. Botero
#        

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------
#   Turbofan NOX Emission Index
# ----------------------------------------------------------------------

def turbofan_nox_emission_index(turbofan, state):
    """ SUAVE.Methods.Propulsion.turbofan_nox_emission_index(turbofan, state)
        correlation taken from Antione, Nicholas, Aircraft Optimization for Minimal Environmental Impact, pp. 31 (PhD Thesis)based on NASA's Engine Performance Program (NEPP)

        Inputs:
            turbofan.combustor
                inputs.
                    stagnation_pressure
                    stagnation_temperature
                outputs.stagnation_temperature
            state

        Outputs:
            nox_emission_index
    """
    
    results = turbofan(state)
    p3      = turbofan.combustor.inputs.stagnation_pressure/Units.psi
    T3      = turbofan.combustor.inputs.stagnation_temperature/Units.degR 
    T4      = turbofan.combustor.outputs.stagnation_temperature/Units.degR
    
    nox_emission_index = .004194*T4*((p3/439.)**.37)*np.exp((T3-1471.)/345.)
    
    #correlation in g Nox/kg fuel; convert to kg Nox/kg
    nox_emission_index = nox_emission_index * (Units.g/Units.kg) 
    
    return nox_emission_index