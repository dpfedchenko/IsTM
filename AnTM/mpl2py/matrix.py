import numpy as np
import matplotlib.pyplot as plt
from assign import Q, pitch, NeC, NoC, Ld, N0, N_pitch, phi_L, phi_R

Pi = np.pi
I = complex (0, 1)

KR = [0.8, 1.2]
NK = 100
kh = (KR[1] - KR[0]) / NK
K = KR[0]

# Functions
def Fe (K, Q, NeC, pitch): return np.exp (I * 2 * Pi * K * pitch/2/Q * NeC)
def Fo (K, Q, NoC, pitch): return np.exp (I * 2 * Pi * K * pitch/2/Q * NoC)
def FeD (K, Ld, N0): return np.exp (I * 2 * Pi * K * Ld/2 * N0)

# Matrix
def Pr (K, Q, NeC, NoC, pitch):
    Fof = Fo (K, Q, NoC, pitch)
    Fef = Fe (K, Q, NeC, pitch)
    return np.diag([1/Fof, Fof, 1/Fef, Fef])

def Dm (NoC, NeC): return np.matrix ([[1, 1, 0, 0], [NoC, -NoC, 0, 0], [0, 0, 1, 1], [0, 0, NeC, -NeC]])

def Di (NoC, NeC): return Dm (NoC, NeC)**(-1)

def R1m (phi):
    C, S = np.cos(phi), np.sin(phi)
    return np.matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def R2i (phi2):
    C, S = np.cos (phi2), np.sin (phi2)
    return R1m (phi2)**(-1)

# Matrix T1
def T1 (delta, K, Q, NeC, NoC, pitch):
    Fof = Fo (K, Q, NoC, pitch)
    Fef = Fe (K, Q, NeC, pitch)
    return np.matrix ([[np.cos(delta)/Fof**2, 0, (-1/2)*(np.sin(delta)*(NoC + NeC))/(Fof*Fef*NoC), (1/2)*(Fef*np.sin(delta)*(-NoC+NeC))/(Fof*NoC)],
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

#
T1f = T1 (2 * Pi/Q, K, Q, NeC, NoC, pitch)
T2f = T2 (0, K, Ld, N0)

#
RmL = R1m (phi_L)
RiR = R2i (phi_R)
##
DmC = Dm (NoC, NeC)
DiC = Di (NoC, NeC)
##
TL = Di (N0, N0)
TR = Dm (N0, N0)

#
U1 = np.zeros (NK)
U2 = np.zeros (NK)

Omega = np.linspace (KR[0], KR[1], NK)

def TO ():
    for i in range (NK):
        K = KR[0] + i * kh
        T1f = T1 (2 * Pi/Q, K, Q, NeC, NoC, pitch)
        T2f = T2 (0, K, Ld, N0)
        
        TCLC = np.dot(RmL, np.dot(DmC, np.dot(np.linalg.matrix_power(T1f, (int(Q * N_pitch))), np.dot(DiC, RiR))))
        TDef = np.dot(RmL, np.dot(DmC, np.dot(T2f, np.dot(DiC, RiR))))
        TT = np.dot(TL, np.dot(TCLC, np.dot(TCLC, np.dot(TDef, np.dot(TCLC, TR)))))

        Vector = np.array([1/np.sqrt(2), 0, -1j/np.sqrt(2), 0])
        
        # СЛУ
        tx = + (+ TT[2,2] * Vector[0] - TT[0,2] * Vector[2]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        ty = - (- TT[0,0] * Vector[2] + TT[2,0] * Vector[0]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        
        U1[i] = abs(tx)**2 + abs(ty)**2
    return U1

def OT ():
    for i in range(NK):
        K = KR[0] + i * kh
        T1f = T1 (2*Pi/Q, K, Q, NeC, NoC, pitch)
        T2f = T2 (0, K, Ld, N0)
        
        TCLC = np.dot(RmL, np.dot(DmC, np.dot(np.linalg.matrix_power(T1f, (int(Q * N_pitch))), np.dot(DiC, RiR))))
        TDef = np.dot(RmL, np.dot(DmC, np.dot(T2f, np.dot(DiC, RiR))))
        TT = np.dot(TL, np.dot(TCLC, np.dot(TDef, np.dot(TCLC, np.dot(TCLC, TR)))))
        
        Vector = np.array([1/np.sqrt(2), 0, -1j/np.sqrt(2), 0])
        
        # СЛУ
        tx = + (+ TT[2,2] * Vector[0] - TT[0,2] * Vector[2]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        ty = - (- TT[0,0] * Vector[2] + TT[2,0] * Vector[0]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        
        U2[i] = abs(tx)**2 + abs(ty)**2   
    return U2

def define_difference(y1, y2, x):
    maxy1 = max(y1)
    maxy2 = max(y2)
    
    idx_maxy1 = np.argmax(y1)
    idx_maxy2 = np.argmax(y2)
    
    wave_length1 = x[idx_maxy1]
    wave_length2 = x[idx_maxy2]
    
    print(f'(TO) Xmax = {wave_length1}')
    print(f'(OT) Xmax = {wave_length2}')
    print(f'Delta TO and OT Xmax = {abs(wave_length2 - wave_length1)}')
    print()
    print(f'Maximum of transmission (TO) = {maxy1}')
    print(f'Maximum of transmission (OT) = {maxy2}')
    print(f'Delta of TO and OT Ymax = {abs(maxy2 - maxy1)}')