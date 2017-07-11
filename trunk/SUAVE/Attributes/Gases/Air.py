# Air.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Gas import Gas
from SUAVE.Core import Data
import numpy as np

# ----------------------------------------------------------------------
#  Air Gas Class
# ----------------------------------------------------------------------

class Air(Gas):

    """ SUAVE.Attributes.Gases.Air()
        Physical constants specific to Air 
    """

    def __defaults__(self):
        """ SUAVE.Attributes.Gases.Air.__defaults__()
            Initializes chemical composition
        """
        self.molecular_mass = 28.96442        # kg/kmol
        self.gas_specific_constant = 287.0528742                 # m^2/s^2-K, specific gas constant
        self.composition.O2 = 0.20946
        self.composition.Ar = 0.00934
        self.composition.CO2 = 0.00036
        self.composition.N2  = 0.78084
        self.composition.other = 0.00

    def compute_density(self,T=300.,p=101325.):
        """ SUAVE.Attributes.Gases.Air.compute_density(T=300.,p=101325.)
            Computes density of air
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                density [kg m^-3]
        """
        return p/(self.gas_specific_constant*T)

    def compute_speed_of_sound(self,T=300.,p=101325.,variable_gamma=False):
        """ SUAVE.Attributes.Gases.Air.compute_speed_of_sound(T=300.,p=101325.,variable_gamma=False)
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
            g = 1.40

        return np.sqrt(g*self.gas_specific_constant*T)

    def compute_cv(self,T=300.,p=101325.):
        """ SUAVE.Attributes.Gases.Air.compute_density(T=300.,p=101325.)
            Not implemented
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
        """
        # placeholder 

        raise NotImplementedError

    def compute_cp(self,T=300.,p=101325.):

        """ SUAVE.Attributes.Gases.Air.compute_cp(T=300.,p=101325.)
            Calculates pressure coefficient    
            3rd-order polynomial data fit:
            cp(T) = c1*T^3 + c2*T^2 + c3*T + c4

            Coefficients (with 95% confidence bounds):
            c1 = -7.357e-007  (-9.947e-007, -4.766e-007)
            c2 =    0.001307  (0.0009967, 0.001617)
            c3 =     -0.5558  (-0.6688, -0.4429)
            c4 =        1074  (1061, 1086) 
            
            cp in J/kg-K, T in K
            Valid for 123 K < T < 673 K 
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                cp - pressure coefficient
            
        """

        c = [-7.357e-007, 0.001307, -0.5558, 1074.0]
        cp = c[0]*T**3. + c[1]*T**2. + c[2]*T + c[3]

        return cp

    def compute_gamma(self,T=300.,p=101325.):

        """ SUAVE.Attributes.Gases.Air.compute_gamma(T=300.,p=101325.)
            Compute specific weight of air
            3rd-order polynomial data fit:
            gamma(T) = c1*T^3 + c2*T^2 + c3*T + c4

            Coefficients (with 95% confidence bounds):
            c1 =  1.629e-010  (1.486e-010, 1.773e-010)
            c2 = -3.588e-007  (-3.901e-007, -3.274e-007)
            c3 =   0.0001418  (0.0001221, 0.0001614)
            c4 =       1.386  (1.382, 1.389)

            gamma dimensionless, T in K
            Valid for 233 K < T < 1273 K 
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                gamma (specific weight) [N/m^3]
        """

        c = [1.629e-010, -3.588e-007, 0.0001418, 1.386]
        g = c[0]*T**3. + c[1]*T**2. + c[2]*T + c[3]

        return g

    def compute_absolute_viscosity(self,T=300.,p=101325.):
        """ SUAVE.Attributes.Gases.Air.compute_absolute_viscosity(T=300.,p=101325.)
            Computes dynamic viscosity with Sutherland's formula
            
            Inputs:
                T - temperature [Kelvin]
                p - pressure [Pa]
                
            Outputs:
                dynamic viscosity [Pa*s]
        """
        S = 110.4                   # constant in deg K (Sutherland's Formula)
        C1 = 1.458e-6               # kg/m-s-sqrt(K), constant (Sutherland's Formula)

        return C1*(T**(1.5))/(T + S)