# Created:  Feb 2015, T. Lukaczyk 
# Modified: Jul 2016, E. Botero 


""" SUAVE Methods for IO """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import DataOrdered

#----------------------------------------------------------------------
# Tree Element
# ----------------------------------------------------------------------

class Tree_Element(DataOrdered):
    """ SUAVE.Input_Output.D3JS.Tree_Element.__init__(name)
        D3.js style tree
    """
    def __init__(self,name):
        """ SUAVE.Input_Output.D3JS.Tree_Element.__init__(name)
            sets name

            Inputs:
                name - string

            Updates:
                self.name
        """
        self.name = name
        
    def append(self,element):
        """ SUAVE.Input_Output.D3JS.Tree_Element.append(element)
            add child to node

            Inputs:
                element - data object

            Updates:
                self.children
        """
        if not 'children' in self:
            self.children = []
        self.children.append(element)