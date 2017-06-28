# Aerodynamics.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff
# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Analyses import Analysis

# default Aero Results
from Results import Results

import numpy as np

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Aerodynamics(Analysis):
    """ SUAVE.Analyses.Aerodynamics.Aerodynamics()
        Abstract aerodynamic model.
    """
    def __defaults__(self):
        self.tag    = 'aerodynamics'
        
        self.geometry = Data()
        self.settings = Data()
        self.settings.maximum_lift_coefficient = np.inf
        
        
    def evaluate(self,state):
        """ SUAVE.Analyses.Aerodyamics.Aerodynamics.evaluate(self, state)
            Evaluates aerodynamics and returns results (to be overrided)
            
            Inputs:
                state - state of the system
                
            Outputs:
                results - all implementations should hold lift and drag coefficients
        """
        
        results = Results()
        
        return results
    
    def finalize(self):
        """ SUAVE.Analyses.Aerodyamics.Aerodynamics.finalize(self, state)
            Does nothing
        """
        
        return
    
    
    def compute_forces(self,conditions):
        """ SUAVE.Analyses.Aerodyamics.Aerodynamics.evaluate(self, state)
            Calculates lift and drag forces
            
            Inputs:
            conditions - conditions in aerodynamic system
                freestream.dynamic_pressure - dynamic pressue in system
                aerodynamics.lift_coefficient - lift coefficient
                aerodynamics.drag_coefficient - drag coefficient
            self - must include reference area
            
            Outputs:
            results - holds lift and drag force vectors
        """
        
        # unpack
        q    = conditions.freestream.dynamic_pressure
        Sref = self.geometry.reference_area
        
        # 
        CL = conditions.aerodynamics.lift_coefficient
        CD = conditions.aerodynamics.drag_coefficient
        
        N = q.shape[0]
        L = np.zeros([N,3])
        D = np.zeros([N,3])

        L[:,2] = ( -CL * q * Sref )[:,0]
        D[:,0] = ( -CD * q * Sref )[:,0]

        results = Data()
        results.lift_force_vector = L
        results.drag_force_vector = D

        return results        
    
        
        
