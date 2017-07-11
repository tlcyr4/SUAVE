# Liquid_H2.py:
#
# Created:  Unk 2013, SUAVE TEAM
# Modified: Apr 2015, SUAVE TEAM
#           Feb 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Propellant import Propellant

# ----------------------------------------------------------------------
#  Liquid_H2 Propellant Class
# ----------------------------------------------------------------------

class Liquid_H2(Propellant):

    """ SUAVE.Attributes.Propellants.Liquid_H2()
        Physical properties of liquid H2 for propulsion use; reactant = O2 
    """

    def __defaults__(self):
        """ SUAVE.Attributes.Propellants.Liquid_H2.__defaults__()
            Initializes propellant properties
        """
        self.tag             = 'Liquid_H2'
        self.reactant        = 'O2'
        self.density         = 59.9                             # kg/m^3
        self.specific_energy = 141.86e6                         # J/kg
        self.energy_density  = 8491.0e6                         # J/m^3