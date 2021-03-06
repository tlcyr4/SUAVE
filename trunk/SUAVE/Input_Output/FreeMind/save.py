# FreeMind.save.py
#
# Created: T. Lukaczyk Feb 2015
# Updated:  

""" SUAVE Methods for IO """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Input_Output import XML
from SUAVE.Core import Data
import time

# ----------------------------------------------------------------------
#  Save!
# ----------------------------------------------------------------------

def save(data,filename):
    """ SUAVE.Input_Output.FreeMind.save(data,filename)
        saves data for freemind

        Inputs:
            data - data object
            filename  - extension should be *.mm
    """
    
    try:
        tag = data.tag
        temp = Data()
        temp[tag] = data
        data = temp
    except AttributeError:
        pass
        
    
    fm_data = XML.Data()
    fm_data.tag = 'map'
    fm_data.attributes.version = "1.0.0"
    
    def build_nodes(prev,data):
        """ SUAVE.Input_Output.FreeMind.save.build_nodes(prev,data)
            recursively builds nodes in freemind datastructure

            Inputs:
                prev - parent or root node
                data - SUAVE data object

            Updates:
                builds prev to be a full tree
        """
        if isinstance(data,dict):
            for key,val in data.items():
                node = new_fm_node(prev,key)
                build_nodes(node,val)
                
        elif isinstance(data,(list,tuple)):
            for val in data:
                build_nodes(prev,val)
                        
        elif not data is None:
            text = str(data)
            node = new_fm_node(prev,text)
            
    build_nodes(fm_data,data)
    
    XML.save(fm_data,filename)
    
    return

def new_fm_node(node,text):
    """ SUAVE.Input_Output.FreeMind.save.new_fm_node(node,text)
        initializes a freemind node

        Inputs:
            node -
    """
    node = node.new_element('node')
    
    node.attributes.TEXT     = text
    
    creation_time = str(int(time.time() * 1000))
    
    node.attributes.CREATED  = creation_time
    node.attributes.MODIFIED = creation_time    
    
    return node