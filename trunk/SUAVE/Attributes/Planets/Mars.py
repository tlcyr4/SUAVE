# Mars.py
# 
# Created:  Unk. 2013, J. Sinsay
# Modified: Apr, 2015, A. Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Planet import Planet

# ----------------------------------------------------------------------
#  Mars Constant Class
# ----------------------------------------------------------------------

class Mars(Planet):
    """ SUAVE.Attributes.Planets.Mars()
        Physical constants specific to Mars and Mars' atmosphere (Obtained from Google)
    """
    def __defaults__(self):
        """ SUAVE.Attributes.Planets.Mars.__defaults__()
            Sets mass, radius, and gravity of Mars
        """
        self.mass              = 639e21 # kg
        self.mean_radius       = 339e4  # m
        self.sea_level_gravity = 3.711  # m/s^2   

