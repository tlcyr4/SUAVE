## @defgroup methods-aerodynamics-Fidelity_Zero-Lift Lift
# Functions to perform low-fidelity lift calculations
# @ingroup methods-aerodynamics-Fidelity_Zero

from weissinger_vortex_lattice import weissinger_vortex_lattice

from compute_max_lift_coeff import compute_max_lift_coeff
from compute_flap_lift import compute_flap_lift
from compute_slat_lift import compute_slat_lift
from vortex_lift import vortex_lift
from linear_inviscid_wing import linear_inviscid_wing

from wing_compressibility_correction import wing_compressibility_correction
from fuselage_correction import fuselage_correction
from aircraft_total import aircraft_total
