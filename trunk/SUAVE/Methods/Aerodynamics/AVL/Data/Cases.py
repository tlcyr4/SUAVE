# Cases.py
# 
# Created:  Oct 2014, T. Momose
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Core import Container as Container_Base

# ------------------------------------------------------------
#  AVL Case
# ------------------------------------------------------------

class Run_Case(Data):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Cases.Run_Case()
        Data structure for an AVL Case
    """
    def __defaults__(self):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Cases.Run_Case.__defaults__()
            Sets default index, tag, mass, conditions, stability_and control, and result_filename

        """

        self.index = 0		# Will be overwritten when passed to an AVL_Callable object
        self.tag   = 'case'
        self.mass  = 0.0

        self.conditions = Data()
        self.stability_and_control = Data()
        free = Data()
        aero = Data()

        free.mach     = 0.0
        free.velocity = 0.0
        free.density  = 1.225
        free.gravitational_acceleration = 9.81

        aero.parasite_drag    = 0.0
        aero.angle_of_attack  = 0.0
        aero.side_slip_angle  = 0.0

        self.stability_and_control.control_deflections = None
        self.conditions.freestream = free
        self.conditions.aerodynamics = aero

        self.result_filename = None


    def append_control_deflection(self,control_tag,deflection):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Cases.Run_Case.append_control_deflection(control_tag,deflection)
            adds a control deflection case 
            
            Inputs:
                control_tag - tag for deflection
                deflection - control deflection
        """
        control_deflection = Data()
        control_deflection.tag        = control_tag
        control_deflection.deflection = deflection
        if self.stability_and_control.control_deflections is None:
            self.stability_and_control.control_deflections = Data()
        self.stability_and_control.control_deflections.append(control_deflection)

        return

class Container(Container_Base):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Cases.Run_Case.Container()
        set of AVL run cases 
    """
    def append_case(self,case):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Cases.Run_Case.Container.append_case(case)
            adds a case to the set of run cases 
            
            Inputs:
                case - AVL case to be added
        """
        case.index = len(self)+1
        self.append(case)
        #case = self.check_new_val(case)
        
        ## store data with the appropriate case index
        ## AVL uses indices starting from 1, not 0!
        ##num_cases = len(self)
        #Data.append(self,case)

        return
    
    
# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------
Run_Case.Container = Container