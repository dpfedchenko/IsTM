import numpy as np
import matplotlib.pyplot as plt

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

def T1(Fo, Fe, No, Ne, phi, phi2):
  return P(Fo, Fe) @ Di(No, Ne) @ R2i(phi2) @ R1m(phi) @ Dm(No, Ne) @ P(Fo, Fe)

def calculate_transmittance(TT):
  Vector = np.array([1 / 2**0.5, 0, -1j / 2**0.5, 0])
  tx =   (+ TT[2, 2] * Vector[0] - TT[0, 2] * Vector[2]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  ty = - (- TT[0, 0] * Vector[2] + TT[2, 0] * Vector[0]) / (- TT[2, 0] * TT[0, 2] + TT[2, 2] * TT[0, 0])
  return [tx, ty]

K = 0
N_sub = 20
LR_def = [0.1197, 1.42 + 0.0075 * 1j]  # L, N

# Define LR_CLC1
LR_CLC1 = [2, 1.57, 1.42, 0.4533, 0]  # L, Ne, No, pitch, phiL + N_pitch, phiR
LR_CLC1[4] = -2 * np.pi * 3 / LR_CLC1[3]

# Define LR_CLC2
LR_CLC2 = LR_CLC1.copy()  # Create a copy to avoid modifying LR_CLC1 directly
LR_CLC2[0] = 3
LR_CLC2[4] = 0

# Build
# LR_sub
LR_sub = [np.sqrt(LR_CLC1[2] * LR_CLC1[3])]
# LR_sub
LR_sub = [np.sqrt(LR_CLC1[2] * LR_CLC1[3])]

# Tf_CLC1
delta_CLC1 = 2 * np.pi * LR_CLC1[0] / LR_CLC1[3] / N_sub
RmL_CLC1 = R1m(LR_CLC1[4])
RiR_CLC1 = R2i(LR_CLC1[4] + 2 * np.pi * LR_CLC1[0] / LR_CLC1[3])
Dm_CLC1 = Dm(LR_CLC1[2], LR_CLC1[1])
Di_CLC1 = Di(LR_CLC1[2], LR_CLC1[1])

delta_CLC2 = 2 * np.pi * LR_CLC2[0] / LR_CLC2[3] / N_sub
RmL_CLC2 = R1m(LR_CLC2[4])
RiR_CLC2 = R2i(LR_CLC2[4] + 2 * np.pi * LR_CLC2[0] / LR_CLC2[3])
Dm_CLC2 = Dm(LR_CLC2[2], LR_CLC2[1])
Di_CLC2 = Di(LR_CLC2[2], LR_CLC2[1])

RmL_def = R1m(0)
RiR_def = R2i(0)
Dm_def = Dm(LR_def[1], LR_def[1])
Di_def = Di(LR_def[1], LR_def[1])

TL = Di(LR_sub[0], LR_sub[0])
TR = Dm(LR_sub[0], LR_sub[0])

# Calc
NK = 1000
KR = [1/0.800, 1/0.600]
U = []
for i in range(NK + 1):
    K = KR[0] + i * (KR[1] - KR[0]) / NK

    Fe_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[1])
    Fo_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[2])
    Tf_CLC1 = P(Fe_CLC1, Fo_CLC1) @ Di(LR_CLC1[2], LR_CLC1[1]) @ R2i(LR_CLC1[4] + delta_CLC1) @ R1m(LR_CLC1[4]) @ Dm(LR_CLC1[2], LR_CLC1[1]) @ P(Fe_CLC1, Fo_CLC1)

    Fe_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[1])
    Fo_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[2])
    Tf_CLC2 = P(Fe_CLC2, Fo_CLC2) @ Di(LR_CLC2[2], LR_CLC2[1]) @ R2i(LR_CLC2[4] + delta_CLC2) @ R1m(LR_CLC2[4]) @ Dm(LR_CLC2[2], LR_CLC2[1]) @ P(Fe_CLC2, Fo_CLC2)

    FeD = np.exp(1j * 2 * np.pi * K * LR_def[0] / 2 * LR_def[1])
    Tf_def = P(FeD, FeD) @ Di(LR_def[1], LR_def[1]) @ R2i(0) @ R1m(0) @ Dm(LR_def[1], LR_def[1]) @ P(FeD, FeD)

    TCLC1 = RmL_CLC1 @ Dm_CLC1 @ np.linalg.matrix_power(Tf_CLC1, N_sub) @ Di_CLC1 @ RiR_CLC1
    TCLC2 = RmL_CLC2 @ Dm_CLC2 @ np.linalg.matrix_power(Tf_CLC2, N_sub) @ Di_CLC2 @ RiR_CLC2
    TDef = RmL_def @ Dm_def @ Tf_def @ Di_def @ RiR_def

    TT = TCLC1 @ TDef @ TCLC2
    TT = TL @ TT @ TR

    tx = calculate_transmittance(TT)[0]
    ty = calculate_transmittance(TT)[1]
    U.append(abs(tx)**2 + abs(ty)**2)

print(U)

t = np.arange(0, NK + 1, 1)
lmbd = 1000 / (KR[0] + (KR[1] - KR[0]) * t / NK)

plt.plot(lmbd[::-1], U[::-1], linewidth = 5, label = 'ATM')
plt.legend()
plt.show()