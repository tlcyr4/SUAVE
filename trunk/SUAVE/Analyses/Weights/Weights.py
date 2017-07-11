# Weights.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from SUAVE.Analyses import Analysis


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Weights(Analysis):
    """ SUAVE.Analyses.Weights.Weights()
        Base analysis for analysing aircraft structures
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Weights.Weights.__defaults__()
            Sets up geometry and settings
        """
        self.tag = 'weights'
        self.vehicle  = Data()
        
        self.settings = Data()
        self.settings.empty_weight_method = \
            SUAVE.Methods.Weights.Correlations.Tube_Wing.empty
        
        
    def evaluate(self,conditions=None):
        """ SUAVE.Analyses.Weights.Weights.evaluate()
            Evaluates weight distribution of vehicle and assigns weight breakdown to vehicle
            see SUAVE.Methods.Weights.Correlations.Tube_Wing.empty
            
            Inputs:
                conditions - conditions of the system
        """
        # unpack
        vehicle = self.vehicle
        empty   = self.settings.empty_weight_method
        
        # evaluate
        results = empty(vehicle)
        
        # storing weigth breakdown into vehicle
        vehicle.weight_breakdown = results 

        # updating empty weight
        vehicle.mass_properties.operating_empty = results.empty
        
        # done!
        return results
    
    
    def finalize(self):
        """ SUAVE.Analyses.Weights.Weights.finalize()
            resets mass properties to match vehicle's
        """
        
        self.mass_properties = self.vehicle.mass_properties
        
        return
        