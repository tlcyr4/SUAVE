#write_sizing_inputs.py
# Created: Jun 2016, M. Vegh


# ----------------------------------------------------------------------
#  Imports
# ---------------

import numpy as np


# ----------------------------------------------------------------------
#  write_sizing_outputs
# ----------------------------------------------------------------------


def write_sizing_outputs(sizing_loop, y_save, opt_inputs):
    """ SUAVE.Sizing.read_sizing_inputs(sizing_loop, opt_inputs)
        Write sizing outputs to a file

        Inputs:
            sizing_loop.output_filename
            y_save
            opt_inputs

        Outputs:
            writes to file
    """
    file=open(sizing_loop.output_filename, 'ab')
    if len(opt_inputs) == 1:
        #weird python formatting issue when writing a 1 entry array
        file.write('[')
        file.write(str(opt_inputs[0]))
        file.write(']')
    else:
        file.write(str(opt_inputs))
    file.write(' ')
    file.write(str(y_save.tolist()))
    file.write('\n') 
    file.close()
                
    return