import cmath
import numpy as np
import IsTM_build as ITMb
import IsTM_plot  as ITMp
from IsTM_materials import SiO2, Air
I, Pi = complex(0, 1), np.pi
SL = [Air, SiO2, Air] * 1
KN, Nsub = 51, 25
Kg = [1]
#Kg = np.linspace(0, 2, KN)

Out = [1, 0]
[zg, E, Tg, ng] = ITMb.goTM(SL, Nsub, Out, Kg)
Ag, Bg = [], []
for i in range(len(E)):
        Ag.append(E[i][0].real)
        Bg.append(E[i][1].real)
        #Ag.append(abs(E[i][0]))
        #Bg.append(abs(E[i][1])) 
ITMp.plotTM(zg, Kg, Ag, Bg, Tg, ng)