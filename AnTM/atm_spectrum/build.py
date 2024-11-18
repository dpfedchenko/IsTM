import numpy as np
from assign import NK, N_sub, KR, LR_def, LR_CLC1, LR_CLC2

# export P, Dm, Di, R1m, R2i, calculate_transmittance 
def P(Fo, Fe):
  return np.diag([1/Fo, Fo, 1/Fe, Fe])

def Dm(No, Ne):
  return np.array([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def Di(No, Ne):
  return np.linalg.inv(Dm(No, Ne))

def R1m(phi):
  C = np.cos(phi)
  S = np.sin(phi)
  return np.array([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def R2i(phi2):
  return np.linalg.inv(R1m(phi2))

def calculate_transmittance(TT):
  Vector = np.array([1 / 2**0.5, 0, -1j / 2**0.5, 0])
  
  Denom = TT[0, 0] * TT[2, 2] - TT[0, 2] * TT[2, 0]

  tx = +(+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / Denom
  ty = -(- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / Denom
  
  rx = (1/2)*(-1j*np.sqrt(2)*TT[0, 0]*TT[1, 2] + 1j*np.sqrt(2)*TT[0, 2]*TT[1, 0] + np.sqrt(2)*TT[1, 0]*TT[2, 2] - np.sqrt(2)*TT[1, 2]*TT[2, 0])/Denom
  ry = (1/2)*(-1j*np.sqrt(2)*TT[0, 0]*TT[3, 2] + 1j*np.sqrt(2)*TT[0, 2]*TT[3, 0] - np.sqrt(2)*TT[2, 0]*TT[3, 2] + np.sqrt(2)*TT[2, 2]*TT[3, 0])/Denom

  return [tx, ty, rx, ry]

#
LR_sub = [np.sqrt(LR_CLC1[1] * LR_CLC1[2])]
lmbd = 1000 / (KR[0] + (KR[1] - KR[0]) * np.arange(0, NK + 1, 1) / NK)

# CLC1_delta_CLC1, RmL_CLC1, RiR_CLC1, Dm_CLC1, Di_CLC1
delta_CLC1 = 2 * np.pi * LR_CLC1[0] / LR_CLC1[3] / N_sub
RmL_CLC1 = R1m(LR_CLC1[4])
RiR_CLC1 = R2i(LR_CLC1[4] + 2 * np.pi * LR_CLC1[0] / LR_CLC1[3])
Dm_CLC1 = Dm(LR_CLC1[2], LR_CLC1[1])
Di_CLC1 = Di(LR_CLC1[2], LR_CLC1[1])

# CLC2_delta_CLC2, RmL_CLC2, RiR_CLC2, Dm_CLC2, Di_CLC2
delta_CLC2 = 2 * np.pi * LR_CLC2[0] / LR_CLC2[3] / N_sub
RmL_CLC2 = R1m(LR_CLC2[4])
RiR_CLC2 = R2i(LR_CLC2[4] + 2 * np.pi * LR_CLC2[0] / LR_CLC2[3])
Dm_CLC2 = Dm(LR_CLC2[2], LR_CLC2[1])
Di_CLC2 = Di(LR_CLC2[2], LR_CLC2[1])

# Defect_RmL_def, RiR_def, Dm_def, Di_def 
RmL_def = R1m(0)
RiR_def = R2i(0)
Dm_def = Dm(LR_def[1], LR_def[1])
Di_def = Di(LR_def[1], LR_def[1])

# TL, TR
TL = Di(LR_sub[0], LR_sub[0])
TR = Dm(LR_sub[0], LR_sub[0])