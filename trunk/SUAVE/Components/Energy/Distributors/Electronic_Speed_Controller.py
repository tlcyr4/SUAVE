# Electronic_Speed_Controller.py
#
# Created:  Jun 2014, E. Botero
# Modified: Jan 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# suave imports
import SUAVE

from SUAVE.Components.Energy.Energy_Component import Energy_Component

# ----------------------------------------------------------------------
#  Electronic Speed Controller Class
# ----------------------------------------------------------------------

class Electronic_Speed_Controller(Energy_Component):
    
    def __defaults__(self):
        
        self.efficiency = 0.0
    
    def voltageout(self,conditions):
        """ SUAVE.Components.Energy.Distributors.Electronic_Speed_Controller.voltageout(conditions)
            The electronic speed controllers voltage out
            
            Inputs:
                conditions.propulsion.throttle - eta - [0-1] throttle setting
               
            Outputs:
                voltsout - voltage out of the ESC

            Properties Used:
                self.inputs.voltagein - a function that returns volts into the ESC

            Updates:
                self.outputs.voltageout - voltage out of the ESC
               
            Assumptions:
                The ESC's output voltage is linearly related to throttle setting
               
        """
        # Unpack, deep copy since I replace values
        eta = (conditions.propulsion.throttle[:,0,None])*1.0
        
        # Negative throttle is bad
        eta[eta<=0.0] = 0.0
        
        # Cap the throttle
        eta[eta>=1.0] = 1.0
        
        voltsin  = self.inputs.voltagein
        voltsout = eta*voltsin
        
        # Pack the output
        self.outputs.voltageout = voltsout
        
        return voltsout
    
    def currentin(self):
        """ SUAVE.Components.Energy.Distributors.Electronic_Speed_Controller.currentin()
            The current going in
            
            Inputs:
                See Properties Used
               
            Outputs:
                Current into the ESC

            Properties Used:
                efficiency - [0-1] efficiency of the ESC
                inputs.currentout

            Updates:
                self.outputs.currentin
               
            Assumptions:
                The ESC draws current.
               
        """
        
        # Unpack
        eff        = self.efficiency
        currentout = self.inputs.currentout
        currentin  = currentout/eff
        
        # Pack
        self.outputs.currentin = currentin
        
        return currentin