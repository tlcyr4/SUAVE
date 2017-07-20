# Aluminum_Air.py
# 
# Created:  Oct 2014, M. Vegh
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE

# package imports
from SUAVE.Core import Units
from SUAVE.Components.Energy.Storages.Batteries  import Battery

# ----------------------------------------------------------------------
#  Battery Class
# ----------------------------------------------------------------------    

class Aluminum_Air(Battery):
    """ SUAVE.Components.Energy.Storages.Batteries.Variable_Mass.Aluminum_Air()
        Variable mass aluminum air battery
    """
    def __defaults__(self):
        self.specific_energy        = 1300.*Units.Wh/Units.kg    # convert to Joules/kg
        self.specific_power         = 0.2*Units.kW/Units.kg      # convert to W/kg
        self.mass_gain_factor       = 0.000110145*Units.kg/Units.Wh
        self.water_mass_gain_factor = 0.000123913*Units.kg/Units.Wh
        self.aluminum_mass_factor   = 0.000123828*Units.kg/Units.Wh # aluminum consumed per energy
        self.ragone.const_1         = 0.8439*Units.kW/Units.kg
        self.ragone.const_2         = -4.8647e-004/(Units.Wh/Units.kg)
        self.ragone.lower_bound     = 1100.*Units.Wh/Units.kg
        self.ragone.upper_bound     = 1600.*Units.Wh/Units.kg
        
    def find_water_mass(self, energy):
        """ SUAVE.Components.Energy.Storages.Batteries.Variable_Mass.Aluminum_Air.find_water_mass(energy)
            Calculare water mass in battery

            Inputs:
                energy

            Outputs:
                water_mass

            Properties Used:
                water_mass_gain_factor
        """
        water_mass = energy*self.water_mass_gain_factor
        return water_mass
        
    def find_aluminum_mass(self, energy):
        """ SUAVE.Components.Energy.Storages.Batteries.Variable_Mass.Aluminum_Air.find_water_mass(energy)
            Calculare aluminum mass in battery

            Inputs:
                energy

            Outputs:
                aluminum_mass

            Properties Used:
                aluminum_mass_factor
        """
        aluminum_mass = energy*self.aluminum_mass_factor
        return aluminum_mass