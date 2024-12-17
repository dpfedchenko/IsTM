import numpy as np
import matplotlib.pyplot as plt
from assign import corrections
from build import lmbd

def T_spectrum_plot(spectral_coefficients):
    for p in range(len(spectral_coefficients)):
        plt.plot(lmbd[::-1], spectral_coefficients[p][0][::-1], linewidth = 3, label = str(corrections[p]))
    plt.ylim(0, 1)
    plt.xlim(560, 660)
    plt.ylabel('Reflectance')
    plt.xlabel('Wavelength, nm')
    plt.legend(loc = 'upper left')
    plt.savefig("Specs1.png", format = 'png', dpi = 300)
    plt.show()