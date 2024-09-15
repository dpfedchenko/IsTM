import matplotlib.pyplot as plt
import numpy as np

def plot_TM(zg, ng, Kg, Tg, E):
    Ag, Bg , sAB = [], [], []
    for i in range(len(E)):
            Ag.append(E[i][0].real)
            Bg.append(E[i][1].real)
            sAB.append(abs(E[i][0] + E[i][1]))
             
    if len(Kg) == 1:
        fig, ax = plt.subplots()
        for i in range (len(zg) - 1):
             ax.plot([zg[i], zg[i + 1]], [ng[i], ng[i + 1]], c = '#00ff00')
        ax.plot(zg, Ag, c = 'r', label = 'A')
        ax.plot(zg, Bg, c = 'b', label = 'B')
        ax.plot(zg, sAB, c = 'm')
        ax.set(xlabel = 'z', ylabel = 'Value')
        ax.legend()
        plt.show()
    else:
        fig, ax = plt.subplots()
        ax.plot(Kg, Tg, c = 'red')
        ax.set(xlabel = 'Wave vector', ylabel = 'Transmittance')
        plt.show()