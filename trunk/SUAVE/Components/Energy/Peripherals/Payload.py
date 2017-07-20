# Payload.py
# 
# Created:  Jun 2014, E. Botero
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE
from SUAVE.Components.Energy.Energy_Component import Energy_Component

# ----------------------------------------------------------------------
#  Payload Class
# ----------------------------------------------------------------------  
    
class Payload(Energy_Component):
    """ SUAVE.Components.Energy.Peripherals.Payload()
        Basically the avionics component
    """
    def __defaults__(self):
        
        self.power_draw = 0.0
        
    def power(self):
        """ SUAVE.Components.Energy.Peripherals.Payload.power()
            The avionics input power
            
            Inputs:
                draw
               
            Outputs:
                power output
               
            Assumptions:
                This device just draws power
               
        """
        self.outputs.power = self.power_draw
        
        return self.power_draw 