# Process.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import ContainerOrdered, DataOrdered
from SUAVE.Analyses.Results import Results

# ----------------------------------------------------------------------
#  Process
# ----------------------------------------------------------------------

class Process(ContainerOrdered):
    """ SUAVE.Analyses.Process
        Discrete piece of the program to be evaluated/executed.  Breaks execution into steps, which are calls to subprocesses or external functions.
    """
    
    verbose = False
    
    def evaluate(self,*args,**kwarg):
        """ SUAVE.Analyses.Process.evaluate(*args,**kwarg)
            execute each step of the process in order and return any results.
            
            Inputs:
                *args, **kwarg - inputs to subprocesses/functions
            
            Outputs:
                results - packaged up results from all subprocesses/functions
        """
        results = Results()
        
        if self.verbose:
            print 'process start'
        
        for tag,step in self.items(): 
            
            if self.verbose:
                print 'step :' , tag
            
            #if not callable(step): continue
            
            if hasattr(step,'evaluate'): 
                result = step.evaluate(*args,**kwarg)
            else:
                result = step(*args,**kwarg)
                
            results[tag] = result
        
        #: for each step
        
        if self.verbose:
            print 'process end'        
        
        return results
        
    def __call__(self,*args,**kwarg):
        """ SUAVE.Analyses.Process.__call__(*args,**kwarg)
            executes process by calling evaluate
            
            Inputs:
                *args, **kwarg - inputs to subprocesses/functions
            
            Outputs:
                results - packaged up results from all subprocesses/functions
        """
        return self.evaluate(*args,**kwarg) 
    
