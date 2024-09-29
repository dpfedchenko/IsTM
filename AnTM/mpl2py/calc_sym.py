from assign import Pi, pitch, Ne, No, Ld, Nd, N0, lmbd, KR
from build import Dm, Di, R1m, R2i, T, Td
from CLC1 import L1, Q1, N_pitch1, phi_L1, phi_R1
from CLC2 import L2, Q2, N_pitch2, phi_L2, phi_R2
import numpy as np

NK = len(lmbd)
kh = 1 / NK

# Precalculate matrices
# CLC1
RmL1 = R1m(phi_L1)
RiR1 = R2i(phi_R1)

# CLC2
RmL2 = R1m(phi_L2)
RiR2 = R2i(phi_R2)

#
DiC = Di(No, Ne)
DmC = Dm(No, Ne)
TL  = Di(N0, N0)
TR  = Dm(N0, N0)

# Function to calculate transmittance coefficient
def calculate_transmittance(TT):
  Vector = np.array([1 / np.sqrt(2), 0, -1j / np.sqrt(2), 0])
  tx = (+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  ty = - (- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  return [tx.tolist(), ty.tolist()] #abs(tx)**2 + abs(ty)**2

# Function to calculate transmittance coefficient for TO
def calculate_TO_sym():
  U1 = np.zeros(NK)
  for i in range(NK):
    K = KR[0] + i * kh
    
    T1f = T(2 * Pi / Q1, K, Q1, Ne, No, pitch)
    T2f = T(2 * Pi / Q2, K, Q2, Ne, No, pitch)
    Tdf = Td(0, K, Ld, Nd)
    
    TCLC1 = RmL1 @ DmC @ T1f**int(Q1 * N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ T2f**int(Q2 * N_pitch2) @ DiC @ RiR2
    TDef  = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    
    TT = TL @ TCLC1 @ TDef @ TCLC2 @ TR
    
    U1[i] = abs(calculate_transmittance(TT)[0])**2 + abs(calculate_transmittance(TT)[1])**2
  return U1

# Function to calculate transmittance coefficient for OT
def calculate_OT_sym():
  U1 = np.zeros(NK)
  for i in range(NK):
    K = KR[0] + i * kh
    
    T1f = T(2 * Pi / Q1, K, Q1, Ne, No, pitch)
    T2f = T(2 * Pi / Q2, K, Q2, Ne, No, pitch)
    Tdf = Td(0, K, Ld, Nd)
    
    TCLC1 = RmL1 @ DmC @ T1f**int(Q1 * N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ T2f**int(Q2 * N_pitch2) @ DiC @ RiR2
    TDef  = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    
    TT = TL @ TCLC2 @ TDef @ TCLC1 @ TR
    
    U1[i] = abs(calculate_transmittance(TT)[0])**2 + abs(calculate_transmittance(TT)[1])**2
  return U1