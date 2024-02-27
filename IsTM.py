# Python libraries
import cmath, numpy as np

# Transfer Matrix modules
import IsTM_build as ITMb
import IsTM_plot as ITMp

# Constants
I, Pi = complex(0, 1), np.pi

# Layers
SiO2 = [3, 0.25/3]
Air =  [1, 0.25]

# Structure
SL = [Air, SiO2, Air] * 1

# TMA
Nsub = 5
Kg = [1]
# Kg = np.linspace(0, 2, 101)
# Kg = 1 + np.linspace(-1, 1, 201)

# Out
Out = [1, 0]

# TM-method
zg = ITMb.goTM(SL, Nsub, Out, Kg)[0]
E = ITMb.goTM(SL, Nsub, Out, Kg)[1]
Tg = ITMb.goTM(SL, Nsub, Out, Kg)[2]

print(zg)

rAg, rBg = [], []
for i in range(len(E)):
        rAg.append(E[i][0].real)
        rBg.append(E[i][1].real) 

# The opposite direction
In  = E[0]

# TM-method
_E = ITMb.goTM(SL[::-1], Nsub, In, Kg)[1]
_Tg = ITMb.goTM(SL[::-1], Nsub, In, Kg)[2]

_rAg, _rBg = [], []
for i in range(len(E)):
        _rAg.append(_E[i][0].real)
        _rBg.append(_E[i][1].real)

ITMp.plotTM(zg, Kg, rAg, rBg, Tg, _rAg, _rBg, _Tg)