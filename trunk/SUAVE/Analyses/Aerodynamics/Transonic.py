# Transonic.py
#
# Created:  Jun 2017, Tigar Cyr
# Modified: 

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------
import SUAVE.Analyses.Aerodynamics.Aerodynamics as Aerodynamics
import SUAVE.Analyses.Aerodynamics.Results as Results
import numpy as np
    
# ----------------------------------------------------------------------
#   Example
# ----------------------------------------------------------------------   \
class Transonic(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Transonic()
        Model based on NASA CRM Transonic Experimental Data
    """
    
    
    def evaluate(self, state):
        # lift model
        # y ~ b1 + b2*x1 + b3*x1^2 + b4*x2 + b5*x2^2 + b6*x3 + b7*x3^2 + b8*x4 + b9*x4^2
        # b = [-435.789730005553 0.742983792057789 -0.421988197961623 0.129666568157724 -0.00512396188693175 8.11823341193399 -68.8488118397378 1.96751918027884 0.00250750492442697]
        # R^2 = .991

        # drag model
        # y ~ b1 + b2*x1 + b3*x1^2 + b4*x2 + b5*x2^2 + b6*x3 + b7*x3^2 + b8*x4 + b9*x4^2
        # b = [8.57222709094397 -0.897800934092333 0.626871359450883 1.78975587167322e-05 0.00131719217498857 -7.33801361840798 119.803398627759 0.144319023849905 -0.00105278583037119]
        # R^2 = .947
        
        
        
        # Initialize results object
        results = Results()
        results.drag = Results()
        results.lift = Results()
        
        # Unpack input
        mach = state.conditions.freestream.mach_number
        alpha = state.conditions.aerodynamics.angle_of_attack
        beta = state.conditons.aerodynamics.side_slip_angle
        phi = state.conditions.aerodynamics.roll_angle
        
        # prepare vector
        predictors = np.array([mach, alpha, beta, phi])
        
        # model coefficients
        bl = np.array([-435.789730005553, 0.742983792057789, -0.421988197961623, 0.129666568157724, -0.00512396188693175, 8.11823341193399, -68.8488118397378, 1.96751918027884, 0.00250750492442697])
        bd = np.array([8.57222709094397, -0.897800934092333, 0.626871359450883, 1.78975587167322e-05, 0.00131719217498857, -7.33801361840798, 119.803398627759, 0.144319023849905, -0.00105278583037119])
        
        # calculate
        cl = bl[0] + predictors * bl[1::2] + np.square(predictors) * bl[2::2]
        cd = bd[0] + predictors * bd[1::2] + np.square(predictors) * bd[2::2]
        
        # Pack up results
        results.drag.total = cd
        results.lift.total = cl
        
        return results
        
