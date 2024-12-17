import numpy as np
from assign import NK, N_sub, KR, layers

def P(Fo, Fe):
  return np.diag([1/Fo, Fo, 1/Fe, Fe])

def Dm(No, Ne):
  return np.array([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def Di(No, Ne):
  return np.linalg.inv(Dm(No, Ne))

def FRm(phi):
  C = np.cos(phi)
  S = np.sin(phi)
  return np.array([[C, 0, S, 0], [0, C, 0, -S], [-S, 0, C, 0], [0, S, 0, C]])

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

def create_layer_matrices(layer):
    """Creates layer matrices based on layer parameters."""
    if layer['name'] == 'CLC1' or layer['name'] == 'CLC2':
        delta = 2 * np.pi * layer['L'] / layer['pitch'] / N_sub
        RmL = R1m(layer['phiL'])
        RiR = R2i(layer['phiL'] + 2 * np.pi * layer['L'] / layer['pitch'])
        Dm_layer = Dm(layer['No'], layer['Ne'])
        Di_layer = Di(layer['No'], layer['Ne'])
        return delta, RmL, RiR, Dm_layer, Di_layer
    elif layer['name'] == 'Defect':
        RmL_def = R1m(0)
        RiR_def = R2i(0)
        Dm_def = Dm(layer['param2'], layer['param2'])
        Di_def = Di(layer['param2'], layer['param2'])
        return 0, RmL_def, RiR_def, Dm_def, Di_def
    else:
        raise ValueError(f"Unknown layer type: {layer['name']}")