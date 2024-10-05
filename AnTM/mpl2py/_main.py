import numpy as np
import matplotlib.pyplot as plt

<<<<<<< Updated upstream
def propagation_matrix(Fo, Fe):
  return np.diag([1/Fo, Fo, 1/Fe, Fe])

def dynamic_matrix(No, Ne):
  return np.array([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])
=======
def Fe(K, L1, N_sub, L2):
    return np.exp(1j * 2 * np.pi * K * L1/N_sub/2 * L2)

def Fo(K, L1, N_sub, L2):
    return np.exp(1j * 2 * np.pi * K * L1/N_sub/2 * L2)
>>>>>>> Stashed changes

def rotation_matrix(phi):
  C = np.cos(phi)
  S = np.sin(phi)
  return np.array([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

<<<<<<< Updated upstream
# Assign variables
K = None  # Unassign 'K'
N_sub = 20

# Define LR_def
LR_def = [0.1197, 1.42 + 0.0075j]

# Define LR_CLC1
=======
def Dm(No, Ne):
    return np.matrix ([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def R1m(phi):
    C, S = np.cos(phi), np.sin(phi)
    return np.matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def calc_T_matrix(delta, No, Ne, K, Q, pitch):
    S, C = sin(delta), cos(delta)
    Fo = F(K, Q, No, pitch)
    Fe = F(K, Q, Ne, pitch)
    return 

def calculate_T_matrix(delta, Fo, Fe, No, Ne):
    S, C = np.sin(delta), np.cos(delta)  
    return np.matrix([
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
    Fo = Fo(K, LR_CLC2[1], N_sub, LR_CLC2[2])
    Fe = Fe(K, Q, Ne, pitch)
    return calculate_T_matrix(delta, Fo, Fe, No, Ne)

def Td(delta, K, Ld, Nd):
    Fo = FeD(K, Ld, Nd)
    Fe = Fo
    return calculate_T_matrix(delta, Fo, Fe, Nd, Nd)

# Assign
N_sub = 50 
LR_def = [0.1197, 1.42 + 0.0075 * 1j]
>>>>>>> Stashed changes
LR_CLC1 = [2, 1.57, 1.42, 0.4533, 0]
LR_CLC1[5] = -2 * np.pi * 3 / LR_CLC1[3]

<<<<<<< Updated upstream
# Define LR_CLC2
LR_CLC2 = LR_CLC1.copy()
LR_CLC2[1] = 3
LR_CLC2[5] = 0
=======
# Build
LR_sub = [(LR_CLC1[2]*LR_CLC1[3])**0.5]
### CLC1
delta = 2 * np.pi * LR_CLC1[0] / LR_CLC1[3] / N_sub
Ne = LR_CLC1[1]
No = LR_CLC1[2]
RmL_CLC1 = R1m(LR_CLC1[4])
RiR_CLC1 = R1m(LR_CLC1[4] + 2 * np.pi * LR_CLC1[0] / LR_CLC1[3])**-1
Dm_CLC1 = Dm(LR_CLC1[1], LR_CLC1[2])
Di_CLC1 = Dm(LR_CLC1[1], LR_CLC1[2])**-1
Tf_CLC1 = calculate_T_matrix(delta, Fo, Fe, LR_CLC1[2], LR_CLC1[1])
>>>>>>> Stashed changes

# Build LR_sub
LR_sub = [np.sqrt(LR_CLC1[2] * LR_CLC1[3])]

# Calculate Tf_CLC1
delta_CLC1 = 2 * np.pi * LR_CLC1[1] / LR_CLC1[4] / N_sub
Fe_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC1[1] / N_sub / 2 * LR_CLC1[2])
Fo_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC1[1] / N_sub / 2 * LR_CLC1[3])
Tf_CLC1 = T1.subs(delta=delta_CLC1, Fe=Fe_CLC1, Fo=Fo_CLC1, Ne=LR_CLC1[2], No=LR_CLC1[3])

# Calculate RmL_CLC1, RiR_CLC1, Dm_CLC1, Di_CLC1
RmL_CLC1 = R1m.subs(phi=LR_CLC1[5])
RiR_CLC1 = R2i.subs(phi2=LR_CLC1[5] + 2 * np.pi * LR_CLC1[1] / LR_CLC1[4])
Dm_CLC1 = Dm.subs(Ne=LR_CLC1[2], No=LR_CLC1[3])
Di_CLC1 = Di.subs(Ne=LR_CLC1[2], No=LR_CLC1[3])

<<<<<<< Updated upstream
# Calculate Tf_CLC2, RmL_CLC2, RiR_CLC2, Dm_CLC2, Di_CLC2
delta_CLC2 = 2 * np.pi * LR_CLC2[1] / LR_CLC2[4] / N_sub
Fe_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[1] / N_sub / 2 * LR_CLC2[2])
Fo_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[1] / N_sub / 2 * LR_CLC2[3])
Tf_CLC2 = T1.subs(delta=delta_CLC2, Fe=Fe_CLC2, Fo=Fo_CLC2, Ne=LR_CLC2[2], No=LR_CLC2[3])
=======
NK = 20
KR = [1/0.720, 1/0.620]
>>>>>>> Stashed changes

RmL_CLC2 = R1m.subs(phi=LR_CLC2[5])
RiR_CLC2 = R2i.subs(phi2=LR_CLC2[5] + 2 * np.pi * LR_CLC2[1] / LR_CLC2[4])
Dm_CLC2 = Dm.subs(Ne=LR_CLC2[2], No=LR_CLC2[3])
Di_CLC2 = Di.subs(Ne=LR_CLC2[2], No=LR_CLC2[3])

<<<<<<< Updated upstream
# Calculate Tf_def, RmL_def, RiR_def, Dm_def, Di_def
FeD = np.exp(1j * 2 * np.pi * K * LR_def[1] / 2 * LR_def[2])
Tf_def = T1.subs(delta=0, Fe=FeD, Fo=FeD, Ne=LR_def[2], No=LR_def[2])

RmL_def = R1m.subs(phi=0)
RiR_def = R2i.subs(phi2=0)
Dm_def = Dm.subs(Ne=LR_def[2], No=LR_def[2])
Di_def = Di.subs(Ne=LR_def[2], No=LR_def[2])

# Calculate TL and TR
TL = Di.subs(Ne=LR_sub[1], No=LR_sub[1])
TR = Dm.subs(Ne=LR_sub[1], No=LR_sub[1])

# Define KR
NK = 20
KR = [1/0.720, 1/0.620]

# Initialize U
U = []

# Loop through K values
for i in range(NK + 1):
  K = KR[0] + i * (KR[1] - KR[0]) / NK

  # Calculate TCLC1, TCLC2, and TDef
  TCLC1 = RmL_CLC1 @ Dm_CLC2 @ np.linalg.matrix_power(Tf_CLC1, N_sub) @ Di_CLC1 @ RiR_CLC1
  TCLC2 = RmL_CLC2 @ Dm_CLC2 @ np.linalg.matrix_power(Tf_CLC2, N_sub) @ Di_CLC2 @ RiR_CLC2
  TDef = RmL_def @ Dm_def @ Tf_def @ Di_def @ RiR_def

  # Calculate TT
  TT = TCLC1 @ TDef @ TCLC2
  TT = TL @ TT @ TR

  # Calculate K1
  K1 = TT @ np.array([tx, 0, ty, 0])

  # Set up equations
  Eq1 = K1[0] - 1/np.sqrt(2)
  Eq2 = K1[1] - rx
  Eq3 = K1[2] + 1j/np.sqrt(2)
  Eq4 = K1[3] - ry

  # Solve for tx, ty, rx, ry
  S = np.linalg.solve(np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]), np.array([Eq1, Eq2, Eq3, Eq4]))
  tx = S[0]
  ty = S[1]
  rx = S[2]
  ry = S[3]

  # Calculate U[i]
  U.append(abs(tx)**2 + abs(ty)**2)

  # Unassign 'i'
i = None

# Create q and q2 lists
q2 = U.copy()  # Copy U to q2
q = [[KR[1] + i * (KR[2] - KR[1]) / NK, U[i]] for i in range(NK + 1)]

# Plot q and q2
plt.plot([x[0] for x in q], [x[1] for x in q], 'bs', markersize=12, label='q')
plt.plot([x[0] for x in q2], [x[1] for x in q2], 'rs', markersize=12, label='q2')

plt.xlabel('k')
plt.ylabel('U')
plt.title('Plot of q and q2')
plt.legend()
plt.show()

# Unassign 'i'
i = None

# Create q and q2 lists for second plot
q2 = U.copy()
q = [[1000 / (KR[1] + i * (KR[2] - KR[1]) / NK), U[i]] for i in range(NK + 1)]

# Plot q and q2
plt.plot([x[0] for x in q], [x[1] for x in q], 'bs', markersize=12, label='q')
plt.plot([x[0] for x in q2], [x[1] for x in q2], 'rs', markersize=12, label='q2')

plt.xlabel('k')
plt.ylabel('U')
plt.title('Plot of q and q2 (Scaled)')
plt.legend()
plt.show()
=======
UTO = np.zeros(NK)
for i in range(NK):
    K = KR[0] + i*(KR[1] - KR[0])/NK
    T1f = T(2 * np.pi / Q1, K, Q1, Ne, No, pitch)
    T2f = T(2 * np.pi / Q2, K, Q2, Ne, No, pitch)
    Tdf = Td(0, K, Ld, Nd)
    TCLC1 = RmL1 @ DmC @ T1f**int(Q1 * N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ T2f**int(Q2 * N_pitch2) @ DiC @ RiR2
    TDef  = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    #
    LR_sub = (Ne *  No)**0.5
    TL = Dm(LR_sub, LR_sub)**-1
    TR = Dm(LR_sub, LR_sub)
    #
    TT = TL @ TCLC1 @ TDef @ TCLC2 @ TR

    UTO[i] = abs(calculate_transmittance(TT)[0])**2 + abs(calculate_transmittance(TT)[1])**2
print(UTO)
>>>>>>> Stashed changes
