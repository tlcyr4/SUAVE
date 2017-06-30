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
import Fidelity_Zero
    
# ----------------------------------------------------------------------
#   Example
# ----------------------------------------------------------------------   \
class Transonic(Aerodynamics):
    """ SUAVE.Analyses.Aerodynamics.Transonic()
        Model based on NASA CRM Transonic Experimental Data
    """
    
    def __defaults__(self):
        self.fzero = Fidelity_Zero.Fidelity_Zero()
        
    
    
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
        beta = state.conditions.aerodynamics.side_slip_angle
        phi = [180] + state.conditions.aerodynamics.roll_angle
        
        first = True
        
        if mach[0,0] < .8:
            if first:
                self.fzero.geometry = self.geometry
                self.fzero.process.compute.lift.inviscid_wings.geometry = self.geometry
                self.fzero.process.compute.lift.inviscid_wings.initialize()
                first = False
            return self.fzero(state)
        else:
        
            # prepare vector
            predictors = np.copy(mach)
            predictors = np.append(predictors, alpha, 1)
            predictors = np.append(predictors, beta, 1)
            predictors = np.append(predictors, phi, 1)
        
            predictors = np.transpose(predictors)
        
            # cl, cd = quadratic_model(predictors)
            cl, cd = quartic_aoa(np.transpose(alpha))
        
        
            """for i in range(len(cl[0])):
            if cl[0,i] < 0 or cd[0,i] < 0:
                printall(i)
            if predictors[1,i] > 10:
                printall(i)
             """   
            # Pack up results
            results.drag.total = np.transpose(cd)
            results.lift.total = np.transpose(cl)
        
        
            return results
    
def quadratic_model(predictors):
        
    # model coefficients
    bl = np.array([[-435.789730005553], [0.742983792057789], [-0.421988197961623], [0.129666568157724], [-0.00512396188693175], [8.11823341193399], [-68.8488118397378], [1.96751918027884], [0.00250750492442697]])
    bd = np.array([[8.57222709094397], [-0.897800934092333], [0.626871359450883], [1.78975587167322e-05], [0.00131719217498857], [-7.33801361840798], [119.803398627759], [0.144319023849905], [-0.00105278583037119]])
            
    # calculate
    cl = bl[0] + np.dot(np.transpose(bl[1::2]), predictors) + np.dot(np.transpose(bl[2::2]), np.square(predictors))
    cd = bd[0] + np.dot(np.transpose(bd[1::2]), predictors) + np.dot(np.transpose(bd[2::2]), np.square(predictors))
            
    return cl, cd
def quartic_aoa(aoa):
    bd = [[.0016], [.00044316],[.0141]]
    bl = [[.000058828], [-.0015], [.00027147], [.1452], [.0980]]
    cd = bd[2] + bd[1] * aoa + bd[0] * np.power(aoa,2)
    if aoa[0,3] > 10:
        print cd[0,3]
    cl = bl[4] + bl[3] * aoa + bl[2] * np.power(aoa,2) + bl[1] * np.power(aoa,3) + bl[0] * np.power(aoa,4)
    return cl, cd
def printall(i):
    print 'predictors'
    print predictors[:,i]
    print 'cl'
    print cl[0,i]
    print 'cd'
    print cd[0,i]
# ----------------------------------------------------------------------
#   Module Testing
# ----------------------------------------------------------------------   
"""import SUAVE.Analyses.Mission.Segments.Conditions.State as State
import SUAVE.Analyses.Mission.Segments.Conditions.Aerodynamics as Aerodynamics

state = State()
state.conditions.update(Aerodynamics())

state.conditions.freestream.mach_number = np.array([[.8503]])
state.conditions.aerodynamics.angle_of_attack = np.array([[-0.7350]])
state.conditions.aerodynamics.side_slip_angle = np.array([[0.0353]])
state.conditions.aerodynamics.roll_angle = np.array([[180.0]])

transonic = Transonic()
result = transonic.evaluate(state)
print result.drag.total
print result.lift.total"""
"""trans = Transonic()

model = Fidelity_Zero.Fidelity_Zero()
model.settings = trans.settings
model.geometry = trans.geometry

model.process.compute.lift.inviscid_wings.geometry = trans.geometry
model.process.compute.lift.inviscid_wings.initialize()

print model.process.compute.lift.inviscid_wings"""



