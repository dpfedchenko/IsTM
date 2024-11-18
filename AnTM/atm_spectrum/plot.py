import numpy as np
import matplotlib.pyplot as plt
from assign import LR_CLC1, LR_CLC2
from build import lmbd
from Berreman import B32_WL, B32_R, B32_T, B32_A
from Berreman import B23_WL, B23_R, B23_T, B23_A

def T_spectrum_plot(T, A, R):
    spectrum_atm = []
    # ATM
    plt.plot(lmbd[::-1], T[::-1], linewidth = 5, c = '#99EE6B', label = 'ATM_T')
    plt.plot(lmbd[::-1], R[::-1], linewidth = 5, c = '#FA7080', label = 'ATM_R')
    plt.plot(lmbd[::-1], A[::-1], linewidth = 5, c = '#64AAD0', label = 'ATM_A')

    # Berreman    
    plt.plot(B32_WL, B32_T, c = '#005500', label = 'B_T')
    plt.plot(B32_WL, B32_R, c = '#550000', label = 'B_R')
    plt.plot(B32_WL, B32_A, c = '#000055', label = 'B_A')
    
    plt.ylim(0, 1)
    plt.xlim(640, 720)
    plt.ylabel('Spectral coefficients')
    plt.xlabel('Wavelength, nm')
    plt.legend(loc='upper left')
    #plt.savefig("Spectrum_" + str(LR_CLC1[0]) + str(LR_CLC2[0]) +  ".png", format = 'png', dpi = 300)
    plt.show()
    return np.array([lmbd[::-1], T[::-1]])