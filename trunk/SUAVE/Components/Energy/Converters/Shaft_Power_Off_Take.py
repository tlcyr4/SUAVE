# Shaft_Power_Off_Take.py
#
# Created:  Jun 2016, L. Kulik

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Components.Energy.Energy_Component import Energy_Component

# package imports
import numpy as np

# ----------------------------------------------------------------------
#  Shaft Power component
# ----------------------------------------------------------------------

class Shaft_Power_Off_Take(Energy_Component):
    """ SUAVE.Components.Energy.Converters.Generator
        an electrical generator component

        this class is callable, see self.__call__

        Inputs:
        power draw

        Outputs:
        work done

        Assumptions:
        This device just draws power

        """
    def __defaults__(self):
        self.power_draw = 0.0
        self.reference_temperature = 288.15
        self.reference_pressure = 1.01325 * 10 ** 5

    def compute(self, state):
        """ SUAVE.Components.Energy.Converters.Shaft_Power_Off_Take.compute(conditions)
            Method called when object is called, computes component output conditions

            Inputs:
                See Properties Used

            Outputs:
                See Updates

            Properties Used:
                power_draw
                inputs.
                    mdhc
                    total_temperature_reference
                    total_pressure_reference
                reference_temperature
                reference_pressure

            Updates:
                self.outputs.
                    power
                    work_done
        """
        if self.power_draw == 0.0:
            self.outputs.work_done = np.array([0.0])

        else:

            mdhc = self.inputs.mdhc
            Tref = self.reference_temperature
            Pref = self.reference_pressure

            total_temperature_reference = self.inputs.total_temperature_reference
            total_pressure_reference    = self.inputs.total_pressure_reference

            self.outputs.power = self.power_draw

            mdot_core = mdhc * np.sqrt(Tref / total_temperature_reference) * (total_pressure_reference / Pref)

            self.outputs.work_done = self.outputs.power / mdot_core

            self.outputs.work_done[mdot_core == 0] = 0

    __call__ = compute
