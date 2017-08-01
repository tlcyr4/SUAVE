# Data.py
#
# Created: T. Lukaczyk Feb 2015
# Updated:  

""" SUAVE Methods for IO """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data as Data_Base

# for enforcing attribute style access names
import string
chars = string.punctuation + string.whitespace
t_table = string.maketrans( chars          + string.uppercase , 
                            '_'*len(chars) + string.lowercase )

# ----------------------------------------------------------------------
#  XML Data Class
# ----------------------------------------------------------------------

class Data(Data_Base):
    """ SUAVE.Input_Output.XML.Data()
        XML format version of a SUAVE Data object
    """
    def __defaults__(self):
        """ SUAVE.Input_Output.XML.Data.__defaults__()
            Initializes some default attributes

            Updates:
                tag
                attributes
                content
                elements
        """
        self.tag        = ''
        self.attributes = Attributes()
        self.content    = ''
        self.elements   = []
        
    def get_elements(self,tag):
        """ SUAVE.Input_Output.XML.Data.get_elements(tag)
            Retrieves elements associated with tag

            Inputs:
                tag

            Outputs:
                output - list of element(s) associated with tag
        """
        output = []
        for e in self.elements:
            if e.tag == tag:
                output.append(e)
        return output
    
    def new_element(self,tag):
        """ SUAVE.Input_Output.XML.Data.new_element(tag)
            Makes a new element associate with tag

            Inputs:
                tag

            Outputs:
                elem - new empty Data() element

            Updates:
                self.elements
        """
        elem = Data()
        elem.tag = tag
        self.elements.append(elem)
        return elem
    
    @staticmethod
    def from_dict(data):
        """ SUAVE.Input_Output.XML.Data.from_dict(data)
            Makes an XML Data object from a dictionary

            Inputs:
                data - dict datastructure

            Outputs:
                result - XML format Data Structure
        """
        result = Data()
        
        if data.has_key('tag'):
            result.tag = data.tag.translate(t_table)
        else:
            result.tag = 'node'
        
        for key,value in data.items():
            if isinstance( value, dict ):
                element = Data.from_dict(value)
                element.tag = key
                result.elements.append(element)
            else:
                element = Data()
                element.tag = key
                element.content = str(value)
                result.elements.append(element)
                
        return result 
         
    def __str__(self,indent=''):
        """ SUAVE.Input_Output.XML.Data.from_dict(data)
            String rep recurses down data structure datanames
        """
        args = ''
        new_indent = '  '
        
        if not indent:
            args += self.dataname()  + '\n'        
        
        # tag
        args += indent + 'tag : %s\n' % self.tag
        
        # attributes
        if self.attributes:
            args += indent + 'attributes : %s' % self.attributes.__str__(indent+new_indent)
        else:
            args += indent + 'attributes : {}\n'
        
        # content
        args += indent + 'content : %s\n' % self.content
        
        # elements
        args += indent + 'elements : '

        # empty elements
        if not self.elements:
            args += '[]\n'
            
        # not empty elements
        else:
            args += '\n'
            indent += new_indent
            
            for i, e in enumerate(self.elements):
                args += indent + '%i :\n' % i
                args += e.__str__(indent + new_indent)
            
        return args
            
            
# ----------------------------------------------------------------------
#  XML Attributes Clas
# ----------------------------------------------------------------------
class Attributes(Data_Base):
    pass