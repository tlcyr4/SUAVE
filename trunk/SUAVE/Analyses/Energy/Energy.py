# Energy.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Analyses import Analysis


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Energy(Analysis):
    """ SUAVE.Analyses.Energy.Energy()
        Base analysis for analysing energy use
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Energy.Energy.__defaults__()
            sets tag to energy
        """
        self.tag     = 'energy'
        self.network = None
        
    def evaluate_thrust(self,state):
        """ SUAVE.Analyses.Energy.Energy.evaluate_thrust()
            calculates the thrust of the network
            
            Inputs:
                state - state of the system (passed to evaluate_thrust)
                
            Outputs:
                results - results of evaluation (returned from evaluate_thrust)
                
            Assumptions:
                network has been instantiated
        """
        network = self.network
        results = network.evaluate_thrust(state) 
        
        return results
    