import numpy as np
# Constants
from assign import Pi, I
# Variables
from assign import Q, pitch, NeC, NoC, Ld, N0, N_pitch, phi_L, phi_R, NK, KR, deg
# Matrix
from build import Dm, Di, R1m, R2i, T1, T2
#
kh = (KR[1] - KR[0]) / NK
K = KR[0]
#
Omega = np.linspace (KR[0], KR[1], NK)
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
#
def TO ():
    for i in range (NK):
        K = KR[0] + i * kh
        # Transfer-matrix
        T1f = T1 (2*Pi/Q, K, Q, NeC, NoC, pitch)
        T2f = T2 (0, K, Ld, N0)
        TCLC = RmL @ DmC @ T1f**int(Q * N_pitch) @ DiC @ RiR
        TDef = RmL @ DmC @ T2f @ DiC @ RiR
        TT = TL @ TCLC**deg @ TDef @ TCLC @ TR
        
        Vector = np.array([1/np.sqrt(2), 0, -1j/np.sqrt(2), 0])
        tx = + (+ TT[2,2] * Vector[0] - TT[0,2] * Vector[2]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        ty = - (- TT[0,0] * Vector[2] + TT[2,0] * Vector[0]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])      
        U1[i] = abs(tx)**2 + abs(ty)**2
    return U1
#
def OT ():
    for i in range(NK):
        K = KR[0] + i * kh
        # Transfer-matrix
        T1f = T1 (2*Pi/Q, K, Q, NeC, NoC, pitch)
        T2f = T2 (0, K, Ld, N0)
        TCLC = RmL @ DmC @ T1f**int(Q * N_pitch) @ DiC @ RiR
        TDef = RmL @ DmC @ T2f @ DiC @ RiR
        TT = TL @ TCLC @ TDef @ TCLC**deg @ TR
        
        Vector = np.array([1/np.sqrt(2), 0, -1j/np.sqrt(2), 0])
        tx = + (+ TT[2,2] * Vector[0] - TT[0,2] * Vector[2]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        ty = - (- TT[0,0] * Vector[2] + TT[2,0] * Vector[0]) / (- TT[2,0] * TT[0,2] + TT[2,2] * TT[0,0])
        U2[i] = abs(tx)**2 + abs(ty)**2   
    return U2
#
def TOOT (y1, y2, x):
    max_y1 = max (y1)
    max_y2 = max (y2)
    
    idx_max_y1 = np.argmax(y1)
    idx_max_y2 = np.argmax(y2)
    
    wave_length1 = x[idx_max_y1]
    wave_length2 = x[idx_max_y2]
    
    print(f'(TO) Xmax = {wave_length1}')
    print(f'(OT) Xmax = {wave_length2}')
    print(f'Delta TO and OT Xmax = {abs(wave_length2 - wave_length1)}')
    print()
    print(f'Maximum of transmission (TO) = {max_y1}')
    print(f'Maximum of transmission (OT) = {max_y2}')
    print(f'Delta of TO and OT Ymax = {abs(max_y2 - max_y1)}')