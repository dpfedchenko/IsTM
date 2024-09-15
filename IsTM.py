import numpy as np
from IsTM_materials import SiO2, Air
from IsTM_calc import calculate_TM
from IsTM_plot import plot_TM

SL = [Air, SiO2, Air] * 2
KN, Nsub = 51, 25

#?
Kg = [1]
#Kg = np.linspace(0, 2, KN)

Out = [1, 0]

[zg, E, Tg, ng] = calculate_TM (SL, Nsub, Out, Kg)
plot_TM (zg, ng, Kg, Tg, E)