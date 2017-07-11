# Steam.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Gas import Gas
from SUAVE.Core import Data

# modules
from math import sqrt


# ----------------------------------------------------------------------
#  Steam Gas Class
# ----------------------------------------------------------------------

class Steam(Gas):

    """ SUAVE.Attributes.Gases.Steam()
        Physical constants specific to steam 
    """

    def __defaults__(self):
        """ SUAVE.Attributes.Gases.Steam.__defaults__()
            Initializes chemical composition
        """
        self.molecular_mass = 18.                  # kg/kmol
        self.gas_specific_constant = 461.889       # m^2/s^2-K, specific gas constant
        self.composition.H2O = 1.0

    def compute_density(self,T=300,p=101325):
        """ SUAVE.Attributes.Gases.Steam.compute_density(T=300.,p=101325.)
            Computes density of steam
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                density [kg m^-3]
        """
        return p/(self.gas_specific_constant*T)

    def compute_speed_of_sound(self,T=300,p=101325,variable_gamma=False):
        """ SUAVE.Attributes.Gases.Steam.compute_speed_of_sound(T=300.,p=101325.,variable_gamma=False)
            Computes speed of sound
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                variable_gamma - whether to recalculate gamma based on other inputs
                
            Outputs:
                speed of sound [m/s]
        """
        if variable_gamma:
            g = self.compute_gamma(T,p)
        else:
            g = 1.33

        return sqrt(g*self.gas_specific_constant*T)

    def compute_cv(self,T=300,p=101325):
        """ SUAVE.Attributes.Gases.Steam.compute_density(T=300.,p=101325.)
            Not implemented
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
        """
        # placeholder 

        raise NotImplementedError

    def compute_cp(self,T=300,p=101325):

        """ SUAVE.Attributes.Gases.Steam.compute_cp(T=300.,p=101325.)
            Calculates pressure coefficient 
            3rd-order polynomial data fit:
            cp(T) = c1*T^3 + c2*T^2 + c3*T + c4


            cp in J/kg-K, T in K
            Valid for 300 K < T < 1500 K 
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                cp - pressure coefficient
        """

        c = [5E-9, -.0001,  .9202, 1524.7]
        cp = c[0]*T**3 + c[1]*T**2 + c[2]*T + c[3]

        return cp

    def compute_gamma(self,T=300,p=101325):
        """ SUAVE.Attributes.Gases.Steam.compute_gamma(T=300.,p=101325.)
            Compute specific weight of air
            No model (yet), just uses 1.33
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                gamma (specific weight) [N/m^3]
        """
        g=1.33                      #use constant value for now; will add a better model later
        
        return g

    def compute_absolute_viscosity(self,T=300,p=101325):
        """ SUAVE.Attributes.Gases.Steam.compute_absolute_viscosity(T=300.,p=101325.)
            Computes dynamic viscosity (uses constant of 1e-6)
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                dynamic viscosity [Pa*s]
        """
        mu0=1E-6

        return mu0