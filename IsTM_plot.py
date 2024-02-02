import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import IsTM_calc

def Tplot (A, B, Str, n1, n2, AB_Out):
    P = len(Str)
    L = 1

    fig, ax = plt.subplots()
    z = np.arange(L/(P + 1), L, L/(P + 1))
    
    maxA = np.max(A)
    maxB = np.max(B)
    maxAB = max(maxA, maxB) 

    ax.plot([0, 0],[L, maxAB], color = 'red', linewidth = 0.2)
    
    for i in range(P + 1):
        if (i != P): 
            ax.plot([(i + 1)/(P + 1), (i + 1)/(P + 1)], [0, maxAB], color = 'red', linestyle = 'dashed', linewidth = 0.2)
        if (i % 2 == 1):
            ax.plot([i/(P + 1), (i + 1)/(P + 1)],[maxAB, maxAB], color = 'red', linestyle = 'dashed', linewidth = 0.2)
        if (i % 2 == 0):
            ax.plot([i/(P + 1), (i + 1)/(P + 1)],[0, 0], color = 'red', linestyle = 'dashed', linewidth = 0.2)
    
    
    for i in range(P):
    #    ax.plot([(i + 1)/(P + 1), (i + 1.5)/(P + 1)], [A[i], A[i]], color = 'green', linewidth = 2.7)
        ax.scatter((i + 1.5)/(P + 1), A[i], linewidth = 2.5, color = 'green', marker = '>')

    for i in range(P):
    #    ax.plot([(i + 1)/(P + 1), (i + 0.5)/(P + 1)], [B[i], B[i]], color = 'red', linewidth = 2.1)
        ax.scatter((i + 0.5)/(P + 1), B[i], linewidth = 2.5, color = 'red', marker = '<')

    Adot = np.delete(A, P)
    ax.plot(z, A[::-1])

    ax.set(xlabel='z', ylabel=' ', title='ITM')
    ax.grid(False)
    #ax.legend()

    plt.show()