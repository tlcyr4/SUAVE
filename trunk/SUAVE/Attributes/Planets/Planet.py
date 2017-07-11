# Planet.py
# 
# Created:  Unk, 2013, J. Sinsay
# Modified: Apr, 2015, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Attributes.Constants import Constant

# ----------------------------------------------------------------------
#  Planet Constant Class
# ----------------------------------------------------------------------
     
class Planet(Constant):
    """ SUAVE.Attributes.Planets.Planet()
        Physical constants of big space rocks 
    """
    def __defaults__(self):
        """ SUAVE.Attributes.Planets.Planet.__defaults__()
            Mass, radius and gravity default to 0
        """
        self.mass              = 0.0  # kg
        self.mean_radius       = 0.0  # m
        self.sea_level_gravity = 0.0  # m/s^2   
