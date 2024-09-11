import numpy as np 

# Constants
Pi = np.pi
I = complex(0, 1)

# List of variables
# Q, pitch, N_pitch, NeC, NoC, Ld, N0

NK = 1000
KR = [0.3, 1.7]

Q = 20
pitch = 1
N_pitch = 8/4

NeC = 11/10
NoC = 1/NeC

N0 = 1
Ld = 1/4

phi_L = 0
phi_R = 2 * Pi * N_pitch

deg = 2