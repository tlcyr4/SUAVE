## @ingroup components-fuselages
# Fuselage.py
# 
# Created:  Mar 2014, T. Lukacyzk
# Modified: Sep 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Components import Physical_Component, Lofted_Body

# ------------------------------------------------------------
#  Fuselage
# ------------------------------------------------------------

## @ingroup components-fuselages
class Fuselage(Lofted_Body):
    """ This is a standard fuselage for a tube and wing aircraft.
    
    Assumptions:
    Conventional fuselage
    
    Source:
    N/A
    """
    
    def __defaults__(self):
        """ This sets the default values for the component to function.
        
        Assumptions:
        None
    
        Source:
        N/A
    
        Inputs:
        None
    
        Outputs:
        None
    
        Properties Used:
        None
        """      
        
        self.tag = 'fuselage'
        self.aerodynamic_center = [0.0,0.0,0.0]
        self.Sections    = Lofted_Body.Section.Container()
        self.Segments    = Lofted_Body.Segment.Container()
        
        self.number_coach_seats = 0.0
        self.seats_abreast      = 0.0
        self.seat_pitch         = 1.0

        self.areas = Data()
        self.areas.front_projected = 0.0
        self.areas.side_projected  = 0.0
        self.areas.wetted          = 0.0
        
        self.effective_diameter = 0.0
        self.width              = 0.0
        
        self.heights = Data()
        self.heights.maximum                        = 0.0
        self.heights.at_quarter_length              = 0.0
        self.heights.at_three_quarters_length       = 0.0
        self.heights.at_vertical_root_quarter_chord = 0.0
        
        self.lengths = Data()
        self.lengths.nose       = 0.0
        self.lengths.tail       = 0.0
        self.lengths.total      = 0.0
        self.lengths.cabin      = 0.0
        self.lengths.fore_space = 0.0
        self.lengths.aft_space  = 0.0
            
        self.fineness = Data()
        self.fineness.nose = 0.0
        self.fineness.tail = 0.0
        
        self.differential_pressure = 0.0
        
        
class Container(Physical_Component.Container):
    pass


# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Fuselage.Container = Container
