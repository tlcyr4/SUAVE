# default_dist.py
#
# Created:  Jul 2017, Tigar Cyr
# Modified: Jul 2017, Tigar Cyr

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------

import numpy as np


def default_dist():
    """ SUAVE.Methods.Aerodynamics.Icing.default_dist()
        Default distribution for icing correction

        Outputs:
            Random non-negative number from a gaussian distribution with mean .1
    """
    return abs(np.random.normal(scale=.1) + .1)