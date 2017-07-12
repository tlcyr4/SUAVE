# Lofted_Body.py
# 
# Created:  
# Modified: Dec 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Component          import Component
from Physical_Component import Physical_Component
from SUAVE.Core         import DataOrdered


# ------------------------------------------------------------
#  Lofted Body
# ------------------------------------------------------------

class Lofted_Body(Physical_Component):
    """ SUAVE.Components.Lofted_Body()
        Geometry composed out of curved and straight line segments
    """
    def __defaults__(self):
        """ SUAVE.Components.Lofted_Body.__defaults__()
            Initializes tag and containers for segments and sections
        """
        self.tag = 'Lofted_Body'
        self.Segments = DataOrdered() # think edges
        self.Sections = SectionContainer() # think nodes
    
   
# ------------------------------------------------------------
#  Segment
# ------------------------------------------------------------

class Segment(Component):
    """ SUAVE.Components.Lofted_Body.Segment()
        Line segment
    """
    def __defaults__(self):
        """ SUAVE.Components.Lofted_Body.Segment.__defaults__()
            Initializes tag and defaults to None for previous and next components
        """
        self.tag = 'Segment'
        
        self.prev = None
        self.next = None # for connectivity

        
# ------------------------------------------------------------
#  Section
# ------------------------------------------------------------

class Section(Component):
    """ SUAVE.Components.Lofted_Body.Section()
        Nodes in the design made up of curves
    """
    def __defaults__(self):
        """ SUAVE.Components.Lofted_Body.Section.__defaults__()
            Initializes tag and defaults to None for previous and next components
        """
        self.tag = 'Section'
        
        self.Curves = CurveContainer()
        
        self.prev = None
        self.next = None
        
# ------------------------------------------------------------
#  Curve
# ------------------------------------------------------------

class Curve(Component):
    """ SUAVE.Components.Lofted_Body.Curve()
        Curved line segment defined by points along it
    """
    def __defaults__(self):
        """ SUAVE.Components.Lofted_Body.Curve.__defaults__()
            Initializes tag and list for holding points
        """
        self.tag = 'Curve'
        self.points = []
        
# ------------------------------------------------------------
#  Containers
# ------------------------------------------------------------


class SectionContainer(Component.Container):
    """ SUAVE.Components.Lofted_Body.Section.Container()
        Container for holding segments
    """
    pass

class CurveContainer(Component.Container):
    """ SUAVE.Components.Lofted_Body.Section.Curve.Container()
        Container for holding curves
    """
    pass


# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------

Section.Curve      = Curve
Section.Container  = SectionContainer
Curve.Container    = CurveContainer
Lofted_Body.Section = Section
Lofted_Body.Segment = Segment
