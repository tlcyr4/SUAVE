# Wing.py
# 
# Created:  Oct 2014, T. Momose
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data

# ------------------------------------------------------------
#   AVL Wing
# ------------------------------------------------------------

class Wing(Data):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing()
        A data class defining the parameters of a wing modeled
        by sections and control surfaces
    """
    def __defaults__(self):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing()
            Default configurations, initializes section and control_surfaces
        """
        self.tag = 'wing'
        self.symmetric = True
        self.vertical  = False
        self.origin    = [0.,0.,0.]

        self.sweep        = 0.0
        self.dihedral     = 0.0

        self.sections = Data()
        self.configuration = Data()
        self.control_surfaces = Data()

        self.configuration.nspanwise = 10
        self.configuration.nchordwise = 5
        self.configuration.sspace = 1.0
        self.configuration.cspace = 1.0


    def append_section(self,section):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.append_section(section)
            adds a segment to the wing 
            
            Inputs:
                section - section to add to wing
        """

        # assert database type
        if not isinstance(section,Data):
            raise Exception, 'input component must be of type Data()'

        # store data
        self.sections.append(section)
        return


# ------------------------------------------------------------
#  AVL Wing Sections
# ------------------------------------------------------------

class Section(Data):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.Section()
        A data class defining an AVL wing section
    """
    def __defaults__(self):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.Section.__defaults__()
            Sets tag, origin, chord, twist, airfoil coord file and control surfaces defaults
        """
        self.tag    = 'section'
        self.origin = [0.0,0.0,0.0]
        self.chord  = 0.0
        self.twist  = 0.0
        self.airfoil_coord_file = None
        self.control_surfaces = Data()
		
				
    def append_control_surface(self,control):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.Section.append_control_surface()
            adds a control_surface to the wing section
            
            Inputs:
                control - control surface
        """

        # assert database type
        if not isinstance(control,Data):
            raise Exception, 'input component must be of type Data()'

        # store data
        self.control_surfaces.append(control)
        return


# ------------------------------------------------------------
#  AVL Control Surface
# ------------------------------------------------------------

class Control_Surface(Data):
    """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.Control_Surface()
        A data class defining an AVL control surface
    """
    def __defaults__(self):
        """ SUAVE.Methods.Aerodynamics.AVL.Data.Wing.Control_Surface.__defaults__()
            Sets default gain, x-hinge coordinate, hinge vector, and sign duplicate
        """
        self.tag            = 'control_surface'
        self.gain           = 1.0
        self.x_hinge        = 0.0
        self.hinge_vector   = [0.,0.,0.]
        self.sign_duplicate = 1.0	# sign_duplicate: 1.0 or -1.0 - the sign of
									# the duplicate control on the mirror wing.
									# Use 1.0 for a mirrored control surface,
									# like an elevator. Use -1.0 for an aileron.

