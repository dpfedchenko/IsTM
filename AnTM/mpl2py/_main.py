import numpy as np

#######
def Fe(K, L1, N_sub, L2):
    return np.exp(1j * 2 * np.pi * K * L1/N_sub/2 * L2)

def Fo(K, L1, N_sub, L2):
    return np.exp(1j * 2 * np.pi * K * L1/N_sub/2 * L2)
#######

def Pr(K, Q, Ne, No, pitch):
    Fo = F (K, Q, No, pitch)
    Fe = F (K, Q, Ne, pitch)
    return diag([Fo**-1, Fo, Fe**-1, Fe])

def Dm(No, Ne):
    return matrix ([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def R1m(phi):
    C, S = cos(phi), sin(phi)
    return matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def calc_T_matrix(delta, No, Ne, K, Q, pitch):
    S, C = sin(delta), cos(delta)
    Fo = F(K, Q, No, pitch)
    Fe = F(K, Q, Ne, pitch)
    return 

def calculate_T_matrix(delta, Fo, Fe, No, Ne):
    S, C = sin(delta), cos(delta)    
    return matrix([
      [C / Fo**2,
       0,
       -.5 * S * (No + Ne) / (Fo * Fe * No),
       .5 * Fe * S * (-No + Ne) / (Fo * No)],
      [0,
       Fo**2 * C,
       .5 * Fo * S * (-No + Ne) / (Fe * No),
       -.5 * Fo * Fe * S * (No + Ne) / No],
      [.5 * S * (No + Ne) / (Fe * Ne * Fo),
      .5 * Fo * S * (-No + Ne) / (Fe * Ne),
      C / Fe**2,
      0],
      [.5 * Fe * S * (-No + Ne) / (Ne * Fo),
      .5 * Fo * Fe * S * (No + Ne) / Ne,
      0,
      Fe**2 * C]])

def T(delta, K, Q, Ne, No, pitch):
    Fo = F(K, Q, No, pitch)
    Fe = F(K, Q, Ne, pitch)
    return calculate_T_matrix(delta, Fo, Fe, No, Ne)

def Td(delta, K, Ld, Nd):
    Fo = FeD(K, Ld, Nd)
    Fe = Fo
    return calculate_T_matrix(delta, Fo, Fe, Nd, Nd)

# Assign
N_sub = 50 
LR_def = [0.1197, 1.42 + 0.0075 * 1j]
LR_CLC1 = [2, 1.57, 1.42, 0.4533, 0]
LR_CLC1[4] = -2 * np.pi * 3/0.4533
LR_CLC2 = LR_CLC1
LR_CLC2[0] = 3
LR_CLC2[4] = 0

# Build
LR_sub = [(LR_CLC1[2]*LR_CLC1[3])**0.5]
### CLC1
delta = 2 * np.pi * LR_CLC1[0] / LR_CLC1[3] / N_sub
Ne = LR_CLC1[1]
No = LR_CLC1[2]
RmL_CLC1 = R1m(LR_CLC1[4])
RiR_CLC1 = R2i(LR_CLC1[4] + 2 * np.pi * LR_CLC1[0] / LR_CLC1[3])
Dm_CLC1 = Dm(LR_CLC1[1], LR_CLC1[2])
Di_CLC1 = Di(LR_CLC1[1], LR_CLC1[2])
Tf_CLC1 = #

### CLC2
delta = 2 * np.pi * LR_CLC2[0]/LR_CLC2[3]/N_sub
Fe = np.exp(1j * 2 * np.pi * K * LR_CLC2[0]/N_sub/2 * LR_CLC2[0])
Fo = np.exp(1j * 2 * np.pi * K * LR_CLC2[0]/N_sub/2 * LR_CLC2[2])
Ne = LR_CLC2[1]
No = LR_CLC2[2]
RmL_CLC2 = R1m(LR_CLC2[4])
RiR_CLC2 = R2i(LR_CLC2[4] + 2 * np.pi * LR_CLC2[0]/LR_CLC2[3])
Dm_CLC2 = Dm(LR_CLC2[1], LR_CLC2[2])
Di_CLC2 = Di(LR_CLC2[1], LR_CLC2[2])
Tf_CLC2 = 0#

###
FeD = np.exp(1j * 2 * np.pi * K * LR_def[0]/2 * LR_def[1]) 
RmL_def = R1m(0)
RiR_def = R2i(0)
Dm_def = Dm(LR_def[1], LR_def[1])
Di_def = Di(LR_def[1], LR_def[1])
Tf_def = 0#

###
TL = Di(LR_sub[1], LR_sub[1])
TR = Dm(LR_sub[1], LR_sub[1])



