import numpy as np
import matplotlib.pyplot as plt
from build import lmbd

def T_spectrum_plot(T):
    plt.plot(lmbd[::-1], T[::-1], linewidth = 5, c = 'r', label = 'ATM')
    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()