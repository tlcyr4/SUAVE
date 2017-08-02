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
        Base aerodynamic model
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Aerodynamics.Aerodynamics.__defaults__()
            Sets up geometry and settings
        """
        self.tag    = 'aerodynamics'
        
        self.geometry = Data()
        self.settings = Data()
        self.settings.maximum_lift_coefficient = np.inf
        
        
    def evaluate(self,state):
        """ SUAVE.Analyses.Aerodynamics.Aerodynamics.evaluate(state)
            evaluates model and returns results (analysis-specific)
            
            Inputs:
                state - state of the system
                
            Outputs:
                results.lift_coefficient - [[0]]
                results.drag_coefficient - [[0]]
                results.lift_force_vector - [[0]]
                results.drag_force_vector - [[0]]

                results - all implementations should hold lift and drag coefficients
        """
        
        results = Results()
        
        return results
    
    def finalize(self):
        """ SUAVE.Analyses.Aerodynamics.Aerodynamics.finalize()
            analysis-specific finalization
        """
        
        return
    
    
    def compute_forces(self,conditions):
        """ SUAVE.Analyses.Aerodynamics.Aerodynamics.compute_forces()
            compute lift and drag forces
            
            Inputs:
                conditions.aerodynamics.lift_coefficient - cl
                conditions.aerodynamics.drag_coefficient - cd
                
            Outputs:
                results.lift_force_vector - lift force vector
                results.drag_force_vector - drag force vector
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
    
        
        
