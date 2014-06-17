""" test_atmosphere.py: test the International Standard Atmopshere model """

import SUAVE
import numpy as np
import matplotlib.pyplot as plt
from SUAVE.Attributes import Units

# main program
def main(block_plot=True):

    # initialize atmospheric models
    atm = SUAVE.Attributes.Atmospheres.Earth.International_Standard()
    
    # test elevations -3 km <= z <= 90 km
    z = np.linspace(-3,90,100) * Units.km

    # compute values from each model
    p, T, rho, a, mew = atm.compute_values(z)

    # plot data
    title = "International Standard Atmosphere"
    plt.subplot(131)
    plt.plot(p/101325,z)
    plt.xlabel('Pressure (atm)'); plt.xscale('log')
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)

    plt.subplot(132)
    plt.plot(rho,z)
    plt.xlabel('Density (kg/m^3)'); plt.xscale('log')
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)

    plt.subplot(133)
    plt.plot(T,z)
    plt.xlabel('Temperature (K)'); 
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)

    plt.show(block=block_plot)
    plt.close()
 
    return

# call main
if __name__ == '__main__':
    main()