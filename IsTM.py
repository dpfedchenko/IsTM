# Python libraries
import cmath, math, numpy as np
import matplotlib.pyplot as plt

# TM modules
import IsTM_matrix as ITMm

# Constants
I, Pi = complex(0, 1), np.pi

# Layers
SiO2 = [3, 0.25/3]
Air =  [1, 0.25]

# Structure
N = 2
SL = ([Air, SiO2]*N + [Air])*2
Nl = len(SL)

# TMA
Nsub = 50
Kg = [1]
# Kg = np.linspace(0, 2, 101)
# Kg = 1 + np.linspace(-1, 1, 101)

# TMB
ng, zg = [], [0]

for i in range(Nl):
    ng += (SL[i][0] * np.ones(Nsub)).tolist()

for i in range(Nl):
    for j in range(Nsub):
        zg.append(zg[-1] + SL[i][1] * math.ceil(j/Nsub)/(Nsub - 1))

zg = zg[1:len(zg)]
dzg = np.diff(np.array(zg))

Tg, Rg, E = [], [], []

# TMC
for k in Kg:
    
    for i in range(len(zg)):
        E.append([0, 0])
    E[-1] = [1, 0]
    
    for j in range(len(zg) - 2, -1, -1):
        if (dzg[j] != 0):
            E[j] = ITMm.iPr(k, ng[j], dzg[j], E[j + 1])
        
        else:
            E[j] = (ITMm.iD(ng[j]) @\
                    ITMm.D(ng[j + 1]) @\
                    np.array(E[j + 1])).tolist()
            
    if len(Kg) == 1:
        rAg, rBg, aAg, aBg, pAg, pBg = [], [], [], [], [], []
        for i in range(len(E)):
            rAg.append(E[i][0].real)
            rBg.append(E[i][1].real) 
            aAg.append(abs(E[i][0]))
            aBg.append(abs(E[i][1]))
            pAg.append(cmath.phase(E[i][0]))
            pBg.append(cmath.phase(E[i][1]))
    else:
        Tg.append(abs(E[-1][0]/E[0][0])**2)
        Rg.append(1 - abs(E[-1][0]/E[0][0])**2)

# TMS
if len(Kg) == 1:
    fig, ax = plt.subplots()
    ax.plot(zg, rAg, color = 'red', label = 'A')
    ax.plot(zg, rBg, color = 'blue', label = 'B')
    ax.set(xlabel='z', ylabel=' ', title='Amplitude and phase')
    ax.set(xlabel='z', ylabel=' ')
    ax.legend()
    plt.show()
else:
    fig, ax = plt.subplots()
    ax.plot(Kg, Tg, color = 'red', label = 'A')
    ax.plot(Kg, Rg, color = 'blue', label = 'B')
    ax.set(xlabel='Wave vector', ylabel='Transmittance', title='Spectrum')
    ax.legend()
    plt.show()