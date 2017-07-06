#load.py
#
# Created:  Jan 2015, T. Lukaczyk
# Modified: Nov 2016, T. MacDonald


""" Load a native SUAVE file """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core.Input_Output import load_data
import json
from SUAVE.Core import Data, DataOrdered
import numpy as np
from collections import OrderedDict

# ----------------------------------------------------------------------
#  Method
# ----------------------------------------------------------------------

def load(filename):
    """ load data from a JSON file containing SUAVE data """
    
    # Get JSON string
    f = open(filename)
    res_string = f.readline()
    f.close()    
    
    # Convert to dictionary
    res_dict = json.loads(res_string,object_pairs_hook=OrderedDict)    
    
    # Convert to SUAVE data structure
    data = read_SUAVE_json_dict(res_dict)
    
    return data

def read_SUAVE_json_dict(res_dict):
    keys = list(res_dict.keys()) # keys from top level
    SUAVE_data = Data() # initialize SUAVE data structure
    
    # Assign all values
    for k in keys:
        k = str(k)
        v = res_dict[k]
        SUAVE_data[k] = build_data_r(v) # recursive function
    return SUAVE_data

def build_data_r(v):
    tv = type(v) # Get value type
    
    # Transform to SUAVE data structure with appropriate types
    if tv == OrderedDict:
        keys = list(v.keys())
        # Recursively assign values
        ret = DataOrdered()
        for k in keys:
            k = str(k)
            ret[k] = build_data_r(v[k])
    elif tv == list:
        ret = np.array(v)
    elif (tv == str): 
        ret = str(v)
    elif (tv == bool):
        ret = v
    elif tv == type(None):
        ret = None
    elif (tv == float) or (tv == int):
        ret = v        
    else:
        raise TypeError('Data type not expected in SUAVE JSON structure')

    return ret