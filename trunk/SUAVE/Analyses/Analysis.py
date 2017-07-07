# Analysis.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Core import Container as ContainerBase
from SUAVE.Analyses import Results


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Analysis(Data):
    """ SUAVE.Analyses.Analysis()
        Base analysis model
    """
    def __defaults__(self):
        self.tag    = 'analysis'
        self.features = Data()
        self.settings = Data()
    
    def compile(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.compile(*args,**kwarg)
            compile the data, settings, etc. avoid analysis specific algorithms
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        return
        
    def initialize(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.initialize(*args,**kwarg)
            analysis specific initialization algorithms
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        return
    
    def evaluate(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.evaluate(*args,**kwarg)
            analysis specific evaluation algorithms
            
            Inputs:
                *args, **kwarg - inputs for evaluation process
            
            Outputs:
                any results of evaluation
        """        
        raise NotImplementedError
        return Results()
    
    def finalize(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.finalize(*args,**kwarg)
            analysis specific finalization algorithms
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """        
        return 
    
    def __call__(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.__call__(*args,**kwarg)
            calls evaluate
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
                
            Outputs:
                results of evaluation process
        """
        return self.evaluate(*args,**kwarg)
    

# ----------------------------------------------------------------------
#  Config Container
# ----------------------------------------------------------------------

class Container(ContainerBase):
    """ SUAVE.Analyses.Analysis.Container()
    """
    
    def compile(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.Container.compile(*args,**kwarg)
            compile all analyses
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        
        for tag,analysis in self.items():
            if hasattr(analysis,'compile'):
                analysis.compile(*args,**kwarg)
        
    def initialize(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.Container.initialize(*args,**kwarg)
            initialize all analyses
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        for tag,analysis in self.items:
            if hasattr(analysis,'initialize'):
                analysis.initialize(*args,**kwarg)
    
    def evaluate(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.Container.evaluate(*args,**kwarg)
            evaluate all analyses
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        results = Results()
        for tag,analysis in self.items(): 
            if hasattr(analysis,'evaluate'):
                result = analysis.evaluate(*args,**kwarg)
            else:
                result = analysis(*args,**kwarg)
            results[tag] = result
        return results
    
    def finalize(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.Container.finalize(*args,**kwarg)
            finalize all analyses
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        for tag,analysis in self.items():
            if hasattr(analysis,'finalize'):
                analysis.finalize(*args,**kwarg)
    
    def __call__(self,*args,**kwarg):
        """ SUAVE.Analyses.Analysis.Container.__call__(*args,**kwarg)
            evaluate container
            
            Inputs:
                *args, **kwarg - inputs for analysis specific implementations
        """
        return self.evaluate(*args,**kwarg)


# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Analysis.Container = Container