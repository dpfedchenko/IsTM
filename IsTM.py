# Python libraries
import cmath
import numpy as np

# Transfer Matrix modules
import IsTM_build as ITMb
import IsTM_plot  as ITMp

# Materials
from IsTM_materials import SiO2, Air

# Constants
I, Pi = complex(0, 1), np.pi

# Structure
SL = [Air, SiO2, Air, SiO2, Air] * 1

#
KN = 101
Nsub = 50

# Wave vector
Kg = [1]
#Kg = np.linspace(0, 2, KN)

# Out vector
Out = [1, 0]

# TM method
[zg, E, Tg, ng] = ITMb.goTM(SL, Nsub, Out, Kg)

Ag, Bg = [], []
for i in range(len(E)):
        Ag.append(E[i][0].real)
        Bg.append(E[i][1].real)
        #Ag.append(abs(E[i][0]))
        #Bg.append(abs(E[i][1]))  

ITMp.plotTM(zg, Kg, Ag, Bg, Tg, ng)