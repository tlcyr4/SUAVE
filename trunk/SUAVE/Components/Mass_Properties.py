# Mass_Properties.py
# 
# Created:  
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data

import numpy as np

# ----------------------------------------------------------------------
#  Mass Properties
# ----------------------------------------------------------------------

class Mass_Properties(Data):
    """ SUAVE.Components.Mass_Properties()
        mass properties for a physical component
    """
    def __defaults__(self):
        """ SUAVE.Components.Mass_Properties.__defaults__()
            defaults mass, volume, cog, and moments of inertia to 0
        """
        self.mass   = 0.0
        self.volume = 0.0
        self.center_of_gravity = np.array([0.0,0.0,0.0])
        
        self.moments_of_inertia = Data()
        self.moments_of_inertia.center = np.array([0.0,0.0,0.0])
        self.moments_of_inertia.tensor = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])