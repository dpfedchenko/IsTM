from assign import pitch, Ne, No, Ld, Nd, N0, lmbd, KR
from build import Dm, R1m, T, Td
from CLC1 import Q1, N_pitch1, phi_L1, phi_R1
from CLC2 import Q2, N_pitch2, phi_L2, phi_R2
import numpy as np

NK = len(lmbd)
kh = (KR[1] - KR[0]) / NK

# Precalculate matrices
# CLC1
RmL1 = R1m(phi_L1)
RiR1 = R1m(phi_R1)**-1
# CLC2
RmL2 = R1m(phi_L2)
RiR2 = R1m(phi_R2)**-1
#
DiC = Dm(No, Ne)**-1
DmC = Dm(No, Ne)
TL  = Dm(N0, N0)**-1
TR  = Dm(N0, N0)

def calculate_transmittance(TT):
  Vector = np.array([1 / 2**0.5, 0, -1j / 2**0.5, 0])
  tx =   (+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  ty = - (- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  return [tx, ty]

def calculate_TO():
  UTO = np.zeros(NK)
  for i in range(NK):
    K = KR[0] + i * kh
    T1f = T(2 * np.pi / Q1, K, Q1, Ne, No, pitch)
    T2f = T(2 * np.pi / Q2, K, Q2, Ne, No, pitch)
    Tdf = Td(0, K, Ld, Nd)
    TCLC1 = RmL1 @ DmC @ T1f**int(Q1 * N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ T2f**int(Q2 * N_pitch2) @ DiC @ RiR2
    TDef  = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    TT = TL @ TCLC1 @ TDef @ TCLC2 @ TR
    UTO[i] = abs(calculate_transmittance(TT)[0])**2 + abs(calculate_transmittance(TT)[1])**2
  return UTO

def calculate_OT():
  UOT = np.zeros(NK)
  for i in range(NK):
    K = KR[0] + i * kh
    T1f = T(2 * np.pi / Q1, K, Q1, Ne, No, pitch)
    T2f = T(2 * np.pi / Q2, K, Q2, Ne, No, pitch)
    Tdf = Td(0, K, Ld, Nd)
    TCLC1 = RmL1 @ DmC @ T1f**int(Q1 * N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ T2f**int(Q2 * N_pitch2) @ DiC @ RiR2
    TDef  = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    TT = TL @ TCLC2 @ TDef @ TCLC1 @ TR
    UOT[i] = abs(calculate_transmittance(TT)[0])**2 + abs(calculate_transmittance(TT)[1])**2
  return UOT