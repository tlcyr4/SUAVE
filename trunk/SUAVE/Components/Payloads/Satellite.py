# Satellite.py
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
#  Sattelite Data Class
# ----------------------------------------------------------------------

class Satellite(Payload):
    """ SUAVE.Components.Payloads.Satellite()
        Satellite payload
    """
    def __defaults__(self):
        self.tag = 'Satellite'