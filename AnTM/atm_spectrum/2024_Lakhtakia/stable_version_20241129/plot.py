import numpy as np
import matplotlib.pyplot as plt
from build import lmbd

def T_spectrum_plot(spectral_coefficients):
    for p in range(len(spectral_coefficients)):
        plt.plot(lmbd[::-1], spectral_coefficients[p][2][::-1], linewidth = 2)
    plt.ylim(0, 1.1)
    plt.xlim(500, 700)
    plt.ylabel('Reflectance')
    plt.xlabel('Wavelength, nm')
    #plt.legend(loc = 'upper left')
    plt.savefig("Specs1.png", format = 'png', dpi = 300)
    plt.show()