# purge_files.py
# 
# Created:  Oct 2014, T. Momose
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import os

def purge_files(filenames_array,directory=''):
    """ SUAVE.Methods.Aerodynamics.AVL.purge_files(filenames_array,directory='')
        Delete a group of files
        
        Inputs:
            filenames_array - files to be deleted
            directory - directory where files are located 
    """
    for f in filenames_array:
		try:
			os.remove(os.path.abspath(os.path.join(directory,f)))
		except OSError:
			pass
			#print 'File {} was not found. Skipping purge.'.format(f)