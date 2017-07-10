# Costs.py
#
# Created:  Sep 2016, T. Orra

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from SUAVE.Analyses import Analysis

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Costs(Analysis):
    """ SUAVE.Analyses.Costs.Costs()
        Base class for analyzing costs of producing and operating vehicles
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Costs.Costs__defaults__()
            Initializes settings with default cost-calculating methods
        """

        self.tag = 'costs'
        self.vehicle  = Data()

        # Default methods to be used
        self.settings = Data()
        self.settings.operating_costs_method = \
            SUAVE.Methods.Costs.Correlations.Operating_Costs.compute_operating_costs
        self.settings.industrial_costs_method = \
            SUAVE.Methods.Costs.Correlations.Industrial_Costs.compute_industrial_costs

    def evaluate(self,conditions=None):
        """ SUAVE.Analyses.Costs.Costs.evaluate(conditions = None)
            Determines manufacturing and operating costs
            
            Inputs:
                conditions - conditions of system
                
            Outputs:
                None
        """

        # unpack
        vehicle             = self.vehicle
        industrial_costs    = self.settings.industrial_costs_method
        operating_costs     = self.settings.operating_costs_method

        # evaluate
        results_manufacturing = industrial_costs(vehicle)
        results_operating     = operating_costs(vehicle)

       # done!
        return

