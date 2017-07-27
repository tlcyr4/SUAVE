# initialize_from_mass.py
# 
# Created:  ### ####, M. Vegh
# Modified: Feb 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------
#  Methods
# ----------------------------------------------------------------------

def initialize_from_mass(battery, mass):
    """ SUAVE.Methods.Power.Battery.Sizing.initialize_from_mass(battery, mass)
        initializes battery based on mass

        Inputs:
            battery.
                specific_energy
                specific_power
            mass

        Outputs:
            See Updates

        Updates:
            battery.
                mass_properties.mass
                max_energy
                max_power
    """
    battery.mass_properties.mass = mass
    battery.max_energy           = mass*battery.specific_energy
    battery.max_power            = mass*battery.specific_power