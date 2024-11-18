import numpy as np
from assign import pitch
# L1, Q1, Q_N_pitch1, N_pitch1, phi_L1, phi_R1 
L1 = 3
Q_N_pitch1 = 165
N_pitch1 = L1 / pitch 
phi_L1 = 0
phi_R1 = 2 * np.pi * N_pitch1 
Q1 = Q_N_pitch1 / N_pitch1