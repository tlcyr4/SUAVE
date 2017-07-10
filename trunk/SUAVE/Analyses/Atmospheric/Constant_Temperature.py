## @ingroup analyses-atmospheric
# Constant_Temperature.py
#
# Created:  Mar 2014, SUAVE Team
# Modified: Feb 2016, A. Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np
from warnings import warn

import SUAVE

from SUAVE.Analyses.Atmospheric import Atmospheric

from SUAVE.Attributes.Gases import Air
from SUAVE.Attributes.Planets import Earth

from SUAVE.Analyses.Mission.Segments.Conditions import Conditions

from SUAVE.Core import Units
from SUAVE.Methods.Utilities import atleast_2d_col


# ----------------------------------------------------------------------
#  Classes
# ----------------------------------------------------------------------
## @ingroup analyses-atmospheric
class Constant_Temperature(Atmospheric):

    """ SUAVE.Analyses.Atmospheric.Constant_Temperature()
        Implements a constant temperature with U.S. Standard Atmosphere (1976 version) freestream pressure
        
        Assumptions:
            None
        
        Source:
            U.S. Standard Atmosphere, 1976, U.S. Government Printing Office, Washington, D.C., 1976
    """
    
    def __defaults__(self):
        """ SUAVE.Analyses.Atmospheric.Constant_Temperature.__defaults__()
            Initializes with default atmosphere properties.  See Atmosphere.py.
            
            Assumptions:
            None
            
            Source:
            N/A
            
            Inputs:
            None
            
            Outputs:
            None
            
            Properties Used:
            None.
        """          
        
        atmo_data = SUAVE.Attributes.Atmospheres.Earth.Constant_Temperature()
        self.update(atmo_data)
    
    def compute_values(self,altitude,temperature=288.15):

        """ SUAVE.Analyses.Atmospheric.Constant_Temperature.compute_values()
            Computes atmospheric values.
        
            Assumptions:
            Constant temperature atmosphere
        
            Source:
            U.S. Standard Atmosphere, 1976, U.S. Government Printing Office, Washington, D.C., 1976
        
            Inputs:
            altitude                                 [m]
            temperature                              [K]
    
            Outputs:
            atmo_data.
              pressure                               [Pa]
              temperature                            [K]
              speed_of_sound                         [m/s]
              dynamic_viscosity                      [kg/(m*s)]
        
            Properties Used:
            self.
              fluid_properties.gas_specific_constant [J/(kg*K)]
              planet.sea_level_gravity               [m/s^2]
              planet.mean_radius                     [m]
              breaks.
                altitude                             [m]
                pressure                             [Pa]
        """

        # unpack
        zs        = altitude
        gas       = self.fluid_properties
        planet    = self.planet
        grav      = self.planet.sea_level_gravity        
        Rad       = self.planet.mean_radius
        gamma     = gas.gas_specific_constant
        
        # check properties
        if not gas == Air():
            warn('Constant_Temperature Atmosphere not using Air fluid properties')
        if not planet == Earth():
            warn('Constant_Temperature Atmosphere not using Earth planet properties')          
        
        # convert input if necessary
        zs = atleast_2d_col(zs)

        # get model altitude bounds
        zmin = self.breaks.altitude[0]
        zmax = self.breaks.altitude[-1]   
        
        # convert geometric to geopotential altitude
        zs = zs/(1 + zs/Rad)
        
        # check ranges
        if np.amin(zs) < zmin:
            print "Warning: altitude requested below minimum for this atmospheric model; returning values for h = -2.0 km"
            zs[zs < zmin] = zmin
        if np.amax(zs) > zmax:
            print "Warning: altitude requested above maximum for this atmospheric model; returning values for h = 86.0 km"   
            zs[zs > zmax] = zmax        

        # initialize return data
        zeros = np.zeros_like(zs)
        p     = zeros * 0.0
        T     = zeros * 0.0
        rho   = zeros * 0.0
        a     = zeros * 0.0
        mew   = zeros * 0.0
        z0    = zeros * 0.0
        T0    = zeros * 0.0
        p0    = zeros * 0.0
        alpha = zeros * 0.0
        
        # populate the altitude breaks
        # this uses >= and <= to capture both edges and because values should be the same at the edges
        for i in range( len(self.breaks.altitude)-1 ): 
            i_inside = (zs >= self.breaks.altitude[i]) & (zs <= self.breaks.altitude[i+1])
            z0[ i_inside ]    = self.breaks.altitude[i]
            T0[ i_inside ]    = temperature
            p0[ i_inside ]    = self.breaks.pressure[i]
            self.breaks.temperature[i+1]=temperature
            alpha[ i_inside ] = -(temperature - temperature)/ \
                                 (self.breaks.altitude[i+1]    - self.breaks.altitude[i])
        
        # interpolate the breaks
        dz = zs-z0
        i_isoth = (alpha == 0.)

        p = p0* np.exp(-1.*dz*grav/(gamma*T0))
       
        T   = temperature
        rho = gas.compute_density(T,p)
        a   = gas.compute_speed_of_sound(T)
        mew = gas.compute_absolute_viscosity(T)
        

                
        atmo_data = Conditions()
        atmo_data.expand_rows(zs.shape[0])
        atmo_data.pressure          = p
        atmo_data.temperature       = T
        atmo_data.density           = rho
        atmo_data.speed_of_sound    = a
        atmo_data.dynamic_viscosity = mew
        
        return atmo_data


# ----------------------------------------------------------------------
#   Module Tests
# ----------------------------------------------------------------------
if __name__ == '__main__':
    
    import pylab as plt
    
    h = np.linspace(-1.,60.,200) * Units.km
    temperature=300
    h = 5000.
    atmosphere = Constant_Temperature()
    
    data = atmosphere.compute_values(h,temperature)
    p   = data.pressure
    T   = data.temperature
    rho = data.density
    a   = data.speed_of_sound
    mew = data.dynamic_viscosity
    
    print data
    