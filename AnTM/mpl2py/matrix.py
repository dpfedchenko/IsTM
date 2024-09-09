import numpy as np

from assign import Q, pitch, NeC, NoC, Ld, N0
from assign import phi_L, phi_R

Pi = np.pi
I = complex(0, 1)
K = 0

# Functions
def Fe (K, Q, NeC, pitch): return np.exp(I * 2 * Pi * K * pitch/2/Q * NeC)
def Fo (K, Q, NoC, pitch): return np.exp(I * 2 * Pi * K * pitch/2/Q * NoC)
def FeD (K, Ld, N0): return np.exp(I * 2 * Pi * K * Ld/2 * N0)

# Matrix
def Pr (K, Q, NeC, NoC, pitch):
    Fo_ = Fo (K, Q, NoC, pitch)
    Fe_ = Fe (K, Q, NeC, pitch)
    return np.diag([1/Fo_, Fo_, 1/Fe_, Fe_])

def Dm (NoC, NeC):
    return np.matrix([[1, 1, 0, 0], [NoC, -NoC, 0, 0], [0, 0, 1, 1], [0, 0, NeC, -NeC]])

def Di (NoC, NeC):
    return Dm(NoC, NeC)**(-1)

def R1m (phi):
    C, S = np.cos(phi), np.sin(phi)
    return np.matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def R2i (phi2):
    C, S = np.cos(phi2), np.sin(phi2)
    return R1m(phi2)**(-1)

# Matrix T1
def T1 (delta, K, Q, NeC, NoC, pitch):
    Fof = Fo(K, Q, NoC, pitch)
    Fef = Fe(K, Q, NeC, pitch)
    return np.matrix([[np.cos(delta)/Fof**2, 0, (-1/2)*(np.sin(delta)*(NoC + NeC))/(Fof*Fef*NoC), (1/2)*(Fef*np.sin(delta)*(-NoC+NeC))/(Fof*NoC)],
                     [0, Fof**2*np.cos(delta), (1/2)*(Fof*np.sin(delta)*(-NoC+NeC))/(Fef*NoC), (-1/2)*Fof*Fef*np.sin(delta)*(NoC+NeC)/NoC],
                     [1/2*(np.sin(delta)*(NoC+NeC))/(Fef*NeC*Fof), 1/2*(Fof*np.sin(delta)*(-NoC+NeC))/(Fef*NeC), np.cos(delta)/Fef**2, 0],
                     [1/2*(Fef*np.sin(delta)*(-NoC+NeC))/(NeC*Fof), 1/2*(Fof*Fef*np.sin(delta)*(NoC+NeC))/NeC, 0, Fef**2 * np.cos(delta)]])

def T2 (delta, K, Ld, N0):
    Fof = FeD (K, Ld, N0)
    Fef = FeD (K, Ld, N0)
    NoC = N0
    NeC = N0
    return np.matrix([[np.cos(delta)/Fof**2, 0, (-1/2)*(np.sin(delta)*(NoC + NeC))/(Fof*Fef*NoC), (1/2)*(Fef*np.sin(delta)*(-NoC+NeC))/(Fof*NoC)],
                     [0, Fof**2*np.cos(delta), (1/2)*(Fof*np.sin(delta)*(-NoC+NeC))/(Fef*NoC), (-1/2)*Fof*Fef*np.sin(delta)*(NoC+NeC)/NoC],
                     [1/2*(np.sin(delta)*(NoC+NeC))/(Fef*NeC*Fof), 1/2*(Fof*np.sin(delta)*(-NoC+NeC))/(Fef*NeC), np.cos(delta)/Fef**2, 0],
                     [1/2*(Fef*np.sin(delta)*(-NoC+NeC))/(NeC*Fof), 1/2*(Fof*Fef*np.sin(delta)*(NoC+NeC))/NeC, 0, Fef**2 * np.cos(delta)]])

###
T1f = T1(2*Pi/Q, K, Q, NeC, NoC, pitch)
T2f = T2(0, K, Ld, N0)

###
RmL = R1m(phi_L)
RiR = R2i(phi_R)
DmC = Dm(NoC, NeC)
DiC = Di(NoC, NeC)
TL = Di(N0, N0)
TR = Dm(N0, N0)

###
KR = [0.97, 1.03]
NK = 50

