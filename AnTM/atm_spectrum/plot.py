import numpy as np
import matplotlib.pyplot as plt
from build import lmbd
from Berreman import tBSp, BSp

def T_spectrum_plot(T1, T2):
    
    plt.plot(lmbd[::-1], T1[::-1], linewidth = 5, c = 'g', label = 'ATM_TO')
    plt.plot(lmbd[::-1], T2[::-1], linewidth = 2, c = 'r', label = 'ATM_OT')
    
    plt.plot(tBSp, BSp, c = 'm', label = 'Berreman')

    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()