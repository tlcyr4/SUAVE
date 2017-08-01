#save.py
#
# Created By:   Trent Jan 2015
# Updated: Carlos Ilario, Feb 2016

""" Save a native SUAVE file """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core.Input_Output import save_data

# ----------------------------------------------------------------------
#  Method
# ----------------------------------------------------------------------

def save(data,filename):
    """ SUAVE.Input_Output.SUAVE.load(filename)
        save data to a file (pickle format)

        Inputs:
            data - data to save
            filename - where to save
    """
    
    save_data(data,filename,file_format='pickle')
    