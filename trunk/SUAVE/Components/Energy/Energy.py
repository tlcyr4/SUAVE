# __init__.py
# 
# Created:  Aug 2014, E. Botero
# Modified: Feb 2016, T. MacDonald

# ------------------------------------------------------------
#  Imports
# ------------------------------------------------------------

from SUAVE.Components import Physical_Component

# ------------------------------------------------------------
#  The Home Energy Container Class
# ------------------------------------------------------------
class Energy(Physical_Component):
    """ SUAVE.Components.Energy.Energy()
        Base Energy component, direct inheritance from Physical_Component
    """
    def __defaults__(self):
        """ SUAVE.Components.Energy.Energy_Component.__defaults__()
            Adds nothing from Physical_Component
        """
        pass


# ------------------------------------------------------------
#  Energy Component Classes
# ------------------------------------------------------------

class Component(Physical_Component):
    """ SUAVE.Components.Energy.Energy.Component()
        Base Energy component, direct inheritance from Physical_Component
    """
    def __defaults__(self):
        """ SUAVE.Components.Energy.Energy_Component.__defaults__()
            Just sets tag
        """
        self.tag = 'Energy Component'
    
    def provide_power():
        pass
    
class ComponentContainer(Physical_Component.Container):
    pass

# ------------------------------------------------------------
#  Handle Linking
# ------------------------------------------------------------
Energy.Component = Component
Energy.Component.Container = ComponentContainer


