# Vehicle.py
#
# Created:
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from Analysis import Analysis


# ----------------------------------------------------------------------
#  Vehicle Analysis
# ----------------------------------------------------------------------

class Vehicle(Analysis.Container):
    """ SUAVE.Analyses.Vehicle()
        All analysis models associated with a vehicle
    """
    def __defaults__(self):
        """ SUAVE.Analyses.Vehicle.__defaults__()
            all models default to None
        """
        self.sizing       = None
        self.weights      = None
        self.aerodynamics = None
        self.stability    = None
        self.energy       = None
        self.atmosphere   = None
        self.planet       = None
        self.noise        = None
        self.costs        = None

    def append(self,analysis):
        """ SUAVE.Analyses.Vehicle.append()
            add an analysis, to be accessed via its root name
            
            Inputs:
                analysis - analysis class
        """

        key = self.get_root(analysis)

        self[key] = analysis


    _analyses_map = None

    def __init__(self,*args,**kwarg):
        """ SUAVE.Analyses.Vehicle.__init__(*args,**kwarg)
            initialize container and map of analyses
            
            Inputs:
                *args, **kwarg - initial values
        """

        Analysis.Container.__init__(self,*args,**kwarg)

        self._analyses_map = {
            SUAVE.Analyses.Sizing.Sizing             : 'sizing'       ,
            SUAVE.Analyses.Weights.Weights           : 'weights'      ,
            SUAVE.Analyses.Aerodynamics.Aerodynamics : 'aerodynamics' ,
            SUAVE.Analyses.Stability.Stability       : 'stability'    ,
            SUAVE.Analyses.Energy.Energy             : 'energy'       ,
            SUAVE.Analyses.Atmospheric.Atmospheric   : 'atmosphere'   ,
            SUAVE.Analyses.Planets.Planet            : 'planet'       ,
            SUAVE.Analyses.Noise.Noise               : 'noise'        ,
            SUAVE.Analyses.Costs.Costs               : 'costs'        ,
        }

    def get_root(self,analysis):
        """ SUAVE.Analyses.Vehicle.get_root(analysis)
            find analysis root by type, allow subclasses
            
            Inputs:
                analysis - analysis class
                
            Outputs:
                analysis_root - root of analysis class from 9 base analyses
        """
        for analysis_type, analysis_root in self._analyses_map.iteritems():
            if isinstance(analysis,analysis_type):
                break
        else:
            raise Exception , "Unable to place analysis type %s" % analysis.typestring()

        return analysis_root


