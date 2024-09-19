import numpy as np
from assign import Pi, Q, pitch, NeC, NoC, Ld, N0, N_pitch, phi_L, phi_R, NK, KR, degTCLC
from build import Dm, Di, R1m, R2i, T1, T2

# Calculate wave vector range
kh = (KR[1] - KR[0]) / NK
K = KR[0]
Omega = np.linspace(KR[0], KR[1], NK)

# Pre-calculate matrices
RmL = R1m(phi_L)
RiR = R2i(phi_R)
DmC = Dm(NoC, NeC)
DiC = Di(NoC, NeC)
TL = Di(N0, N0)
TR = Dm(N0, N0)

# Initialize output arrays
U1 = np.zeros(NK)
U2 = np.zeros(NK)

# Function to calculate transmittance coefficient
def calculate_transmittance(TT):
  Vector = np.array([1 / np.sqrt(2), 0, -1j / np.sqrt(2), 0])
  tx = (+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  ty = - (- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  return abs(tx)**2 + abs(ty)**2

# Function to calculate transmittance coefficient for TO
def calculate_TO():
  for i in range(NK):
    K = KR[0] + i * kh
    T1f = T1(2 * Pi / Q, K, Q, NeC, NoC, pitch)
    T2f = T2(0, K, Ld, N0)
    TCLC = RmL @ DmC @ T1f**int(Q * N_pitch) @ DiC @ RiR
    TDef = RmL @ DmC @ T2f @ DiC @ RiR
    TT = TL @ TCLC**degTCLC[0] @ TDef @ TCLC**degTCLC[1] @ TR
    U1[i] = calculate_transmittance(TT)
  return U1

# Function to calculate transmittance coefficient for OT
def calculate_OT():
  for i in range(NK):
    K = KR[0] + i * kh
    T1f = T1(2 * Pi / Q, K, Q, NeC, NoC, pitch)
    T2f = T2(0, K, Ld, N0)
    TCLC = RmL @ DmC @ T1f**int(Q * N_pitch) @ DiC @ RiR
    TDef = RmL @ DmC @ T2f @ DiC @ RiR
    TT = TL @ TCLC**degTCLC[1] @ TDef @ TCLC**degTCLC[0] @ TR
    U2[i] = calculate_transmittance(TT)
  return U2