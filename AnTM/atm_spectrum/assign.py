import numpy as np

# export NK, N_sub, KR, LR_def, LR_CLC1, LR_CLC2
NK = 2000
N_sub = 2000
KR = [1/0.820, 1/0.560]

# L, Ne, No, pitch, phiL + N_pitch
LR_CLC1 = [3, 1.57, 1.42, 0.4533, 0] 
LR_CLC1[4] = -2 * np.pi * 3 / LR_CLC1[3]

LR_CLC2 = [2, 1.57, 1.42, 0.4533, 0]
LR_CLC2[4] = 0

LR_def = [0.1197, 1.42 + 0.0075 * 1j]