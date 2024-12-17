import numpy as np
from assign import NK, N_sub, KR, perturb_layers

def P(Fo, Fe): return np.diag([1/Fo, Fo, 1/Fe, Fe])

def Dm(No, Ne): return np.array([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def Di(No, Ne): return np.linalg.inv(Dm(No, Ne))

def FRm(phi):
  C, S = np.cos(phi), np.sin(phi)
  return np.array([[C, 0, S, 0], [0, C, 0, -S], [-S, 0, C, 0], [0, S, 0, C]])

def R1m(phi):
  C, S = np.cos(phi), np.sin(phi)
  return np.array([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def R2i(phi2): return np.linalg.inv(R1m(phi2))

def calculate_transmittance(TT):
  Vector = np.array([1 / 2**0.5, 0, -1j / 2**0.5, 0])
  Denom = TT[0, 0] * TT[2, 2] - TT[0, 2] * TT[2, 0]
  tx = +(+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / Denom
  ty = -(- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / Denom
  rx = (1/2)*(-1j*np.sqrt(2)*TT[0, 0]*TT[1, 2] + 1j*np.sqrt(2)*TT[0, 2]*TT[1, 0] + np.sqrt(2)*TT[1, 0]*TT[2, 2] - np.sqrt(2)*TT[1, 2]*TT[2, 0])/Denom
  ry = (1/2)*(-1j*np.sqrt(2)*TT[0, 0]*TT[3, 2] + 1j*np.sqrt(2)*TT[0, 2]*TT[3, 0] - np.sqrt(2)*TT[2, 0]*TT[3, 2] + np.sqrt(2)*TT[2, 2]*TT[3, 0])/Denom
  return [tx, ty, rx, ry]

def clc_layer(K, lr_clc, delta_clc):
    Fe_clc = np.exp(1j * 2 * np.pi * K * lr_clc[0] / N_sub / 2 * lr_clc[1])
    Fo_clc = np.exp(1j * 2 * np.pi * K * lr_clc[0] / N_sub / 2 * lr_clc[2])
    return P(Fo_clc, Fe_clc) @ Di(lr_clc[2], lr_clc[1]) @ R2i(lr_clc[4] + delta_clc) @ R1m(lr_clc[4]) @ Dm(lr_clc[2], lr_clc[1]) @ P(Fe_clc, Fo_clc)

lmbd = 1000 / (KR[0] + (KR[1] - KR[0]) * np.arange(0, NK + 1, 1) / NK)
LR_sub = [np.sqrt(perturb_layers[0][0][1] * perturb_layers[0][0][2])]

TL = Di(LR_sub[0], LR_sub[0])
TR = Dm(LR_sub[0], LR_sub[0])

def layer_parameters(layer):
  delta = 2 * np.pi * layer[0] / layer[3] / N_sub
  RmL = R1m(layer[4])
  RiR = R2i(layer[4] + 2*np.pi*layer[0] / layer[3])
  DmM = Dm(layer[2], layer[1])
  DiM = Di(layer[2], layer[1])
  return delta, RmL, RiR, DmM, DiM