# Icing.py
#
# Created:  Jul 2017, Tigar Cyr
# Modified: Jul 2017, Tigar Cyr

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Transonic as Transonic
import numpy as np
from SUAVE.Methods.Aerodynamics import Icing as Methods


# ----------------------------------------------------------------------
#   Icing
# ----------------------------------------------------------------------
class Icing(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Icing()
        Model based on NASA CRM Transonic Experimental Data (curve fits)
        With corrections for effects of icing
    """
    def __init__(self, model = Transonic.Transonic(), cl_dist = Methods.default_dist.default_dist, cd_dist = Methods.default_dist.default_dist):
        self.model = model
        self.cl_dist = cl_dist
        self.cd_dist = cd_dist

        self.reset()



    def adjust_cl(self, cl):
        """ SUAVE.Analyses.Aerodynamics.Icing.adjust_cl(cl)
            Corrects lift coefficient for losses due to icing

            Inputs:
                cl - lift coefficient

            Outputs:
                adjusted lift coefficient
        """
        return cl - self.cl_adjust

    def adjust_cd(self, cd):
        """ SUAVE.Analyses.Aerodynamics.Icing.adjust_cd(cd)
            Corrects drag coefficient for losses due to icing

            Inputs:
                cd - drag coefficient

            Outputs:
                adjusted drag coefficient
        """
        return cd #+ self.cd_adjust

    def reset(self):
        """ SUAVE.Analyses.Aerodynamics.Icing.adjust_cd(cd)
            Resamples correction distributions

            Properties Used:
                cl_dist - cl adjustment distribution
                cd_dist - cd adjustment distribution

            Updates:
                self.cl_adjust
                self.cd_adjust
        """
        self.cl_adjust = self.cl_dist()
        self.cd_adjust = self.cd_dist()



    def evaluate(self, state):
        """ SUAVE.Analyses.Aerodynamics.Icing.evaluate(state)
            evaluate aerodynamic analysis

            Inputs: (depends on model used, showing for default)
                state.conditions.freestream.mach_number - mach number
                state.conditions.aerodynamics.angle_of_attack - aoa [radians]

            Outputs:
                results.lift.total - lift coefficient
                results.drag.total - drag coefficient

            Properties Used:
                adjust_cl
                adjust_cd
                model
        """

        results = self.model(state)

        results.lift.total = self.adjust_cl(results.lift.total)
        results.drag.total = self.adjust_cd(results.drag.total)

        return results


# ----------------------------------------------------------------------
#   Module Testing
# ----------------------------------------------------------------------
def main():
    import SUAVE.Analyses.Mission.Segments.Conditions.State as State
    import SUAVE.Analyses.Mission.Segments.Conditions.Aerodynamics as Aerodynamics
    import SUAVE.Analyses.Aerodynamics.Fidelity_Zero as Fidelity_Zero

    state = State()
    state.conditions.update(Aerodynamics())

    state.conditions.freestream.mach_number = np.array([[.8503], [.85], [.85]])
    state.conditions.aerodynamics.angle_of_attack = np.array([[0], [1], [2]])
    state.conditions.aerodynamics.side_slip_angle = np.array([[0], [0], [0]])
    state.conditions.aerodynamics.roll_angle = np.array([[180.0], [180], [180]])

    # model = Fidelity_Zero()
    # model.settings.drag_coefficient_increment = 0.0000
    # model.landing.aerodynamics.settings.spoiler_drag_increment = 0.00
    # model.geometry = trans.geometry
    # transonic = Transonic_Icing(model)
    # result = transonic.evaluate(state)
    # print result.drag.total
    # print result.lift.total
    # print transonic.settings.maximum_lift_coefficient




#
#    model.process.compute.lift.inviscid_wings.geometry = trans.geometry
#    model.process.compute.lift.inviscid_wings.initialize()
#
#    print model.process.compute.lift.inviscid_wings

if __name__ == '__main__':
    main()

