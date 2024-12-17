import numpy as np

NK = 1000
N_sub = 1000
KR = [1/0.800, 1/0.560]

# L, Ne, No, pitch, phiL + N_pitch
LR_CLC1 = [3, 1.57, 1.4215, 0.454, 0] 
LR_CLC1[4] = -2 * np.pi * LR_CLC1[0] / LR_CLC1[3]

LR_CLC2 = [2, 1.57, 1.4215, 0.454, 0]
LR_CLC2[4] = 0

LR_def = [0.1197, 1.4215 + 0.0075 * 1j, 0, 0, 0]