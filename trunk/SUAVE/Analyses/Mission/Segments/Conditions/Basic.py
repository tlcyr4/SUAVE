# Basic.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# python imports
import numpy as np

# SUAVE imports
from Conditions import Conditions

# ----------------------------------------------------------------------
#  Conditions
# ----------------------------------------------------------------------

class Basic(Conditions):
    """ SUAVE.Analyses.Mission.Segments.Basic()
        Basic conditions for analysing a general physical system
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Mission.Segments.Basic.__defaults__()
            initializes weights, frames and energies conditions (all array values at 0)
        """
        self.tag = 'basic_conditions'
        
        # start default row vectors
        ones_1col = self.ones_row(1)
        ones_2col = self.ones_row(2)
        ones_3col = self.ones_row(3)
        
        # top level conditions
        self.frames   = Conditions()
        self.weights  = Conditions()
        self.energies = Conditions()
        
        # inertial conditions
        self.frames.inertial = Conditions()        
        self.frames.inertial.position_vector      = ones_3col * 0
        self.frames.inertial.velocity_vector      = ones_3col * 0
        self.frames.inertial.acceleration_vector  = ones_3col * 0
        self.frames.inertial.gravity_force_vector = ones_3col * 0
        self.frames.inertial.total_force_vector   = ones_3col * 0
        self.frames.inertial.time                 = ones_1col * 0
        
        # body conditions
        self.frames.body = Conditions()        
        self.frames.body.inertial_rotations       = ones_3col * 0
        self.frames.body.transform_to_inertial    = np.empty([0,0,0])
        
        
        # weights conditions
        self.weights.total_mass            = ones_1col * 0
        self.weights.weight_breakdown      = Conditions()
        
        # energy conditions
        self.energies.total_energy         = ones_1col * 0
        self.energies.total_efficiency     = ones_1col * 0