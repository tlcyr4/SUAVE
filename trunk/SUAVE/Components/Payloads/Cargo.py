# Cargo.py
# 
# Created:  
# Modified: Feb 2016, T. MacDonald

""" SUAVE Vehicle container class 
    with database + input / output functionality 
"""


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Payload import Payload

# ----------------------------------------------------------------------
#  Cargo Data Class
# ----------------------------------------------------------------------

class Cargo(Payload):
    """ SUAVE.Components.Payloads.Cargo()
        Cargo payload
    """
    def __defaults__(self):
        self.tag = 'Cargo'
