# Process_Geometry.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Analyses import Process, Results

# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Process_Geometry(Process):
    """ SUAVE.Analyses.Aerodynamics.Process_Geometry()
        Process for evaluation based on a specific subset of geometry
    """
    geometry_key = None
    
    def __init__(self,geometry_key):
        """ SUAVE.Analyses.Aerodynamics.Process_Geometry.__init__(geometry_key)
            initializes geometry key
            
            Inputs:
                geometry_key - key for subset of geometry
        """
        self.geometry_key = geometry_key
    
    def evaluate(self,state,settings,geometry):
        """ SUAVE.Analyses.Aerodynamics.Process_Geometry.evaluate(state, settings. geometry)
            Evaluate all subprocesses/methods passing them a specific part of geometry
            
            Inputs:
                state - state of the system
                settings - settings for analysis
                geometry - overall geometry
                
            Outputs:
                results - results of process execution
        """
        
        #
        geometry_items = geometry.deep_get(self.geometry_key)
        
        results = Results()
        
        for key, this_geometry in geometry_items.items():
            result = Process.evaluate(self,state,settings,this_geometry)
            results[key] = result
            
        return results
        
        
        
        