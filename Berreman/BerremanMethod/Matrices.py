import numpy as np

#Const
I = complex(0, 1)
Pi = np.pi

def R1m_matrix(L, pitch):
    
    N_pitch = L / pitch
    phi = 2 * np.pi * N_pitch
    
    R1m = np.zeros((4, 4))
    
    R1m[0][0] = np.np.cos(phi)
    R1m[0][1] = 0
    R1m[0][2] = np.sin(phi)
    R1m[0][3] = 0

    R1m[1][0] = 0
    R1m[1][1] = np.cos(phi)
    R1m[1][2] = 0
    R1m[1][3] = np.sin(phi)

    R1m[2][0] = -np.sin(phi)
    R1m[2][1] = 0
    R1m[2][2] = np.cos(phi)
    R1m[2][3] = 0

    R1m[3][0] = 0 
    R1m[3][1] = -np.sin(phi) 
    R1m[3][2] = 0 
    R1m[3][3] = np.cos(phi)
    
    return R1m

def R2i_matrix(L, pitch):
    
    N_pitch = L / pitch
    phi_R = 2 * np.pi * N_pitch
    phi2 = phi_R
    
    R2i = np.zeros((4, 4))
    
    R2i[0][0] = np.np.cos(phi2)
    R2i[0][1] = 0
    R2i[0][2] = -np.sin(phi2)
    R2i[0][3] = 0

    R2i[1][0] = 0
    R2i[1][1] = np.cos(phi2)
    R2i[1][2] = 0
    R2i[1][3] = -np.sin(phi2)

    R2i[2][0] = np.sin(phi2)
    R2i[2][1] = 0
    R2i[2][2] = np.cos(phi2)
    R2i[2][3] = 0

    R2i[3][0] = 0 
    R2i[3][1] = np.sin(phi2) 
    R2i[3][2] = 0 
    R2i[3][3] = np.cos(phi2)
    
    return R2i

def Dm_matrix(No, Ne):
    
    Dm = np.zeros((4, 4))
    
    Dm[0][0] = 1
    Dm[0][1] = 1
    Dm[0][2] = 0
    Dm[0][3] = 0

    Dm[1][0] = No
    Dm[1][1] = -No
    Dm[1][2] = 0
    Dm[1][3] = 0

    Dm[2][0] = 0
    Dm[2][1] = 0
    Dm[2][2] = 1
    Dm[2][3] = 1

    Dm[3][0] = 0 
    Dm[3][1] = 0 
    Dm[3][2] = Ne 
    Dm[3][3] = -Ne
    
    return Dm

def Di_matrix(No, Ne):
    
    Di = np.zeros((4, 4))
    
    Di[0][0] = 1/2
    Di[0][1] = 1/(2*No)
    Di[0][2] = 0
    Di[0][3] = 0

    Di[1][0] = 1/2
    Di[1][1] = -1/(2*No)
    Di[1][2] = 0
    Di[1][3] = 0

    Di[2][0] = 0
    Di[2][1] = 0
    Di[2][2] = 1/2
    Di[2][3] = 1/(2*Ne)

    Di[3][0] = 0 
    Di[3][1] = 0 
    Di[3][2] = 1/2
    Di[3][3] = -1/(2*Ne)
    
    return Di

def T1_matrix(K, pitch, Q_N_pitch1, L1, NoC, NeC):   
    
    N_pitch1 = L1 / pitch
    Q1 = Q_N_pitch1 / N_pitch1
    
    delta = 2 * np.pi / Q1
    
    Fo = np.exp(I*2*Pi*K*pitch/Q1*NoC)
    Fe = np.exp(I*2*Pi*K*pitch/Q1*NeC)
    
    No = NoC
    Ne = NeC
    
    T1 = np.zeros((4, 4))

    T1[0][0] = np.cos(delta)/Fo 
    T1[0][1] = 0
    T1[0][2] = -(1/2)*np.sin(delta)*(No+Ne)/(No*Fe)
    T1[0][3] = (1/2)*Fe*np.sin(delta)*(-No+Ne)/No

    T1[1][0] = 0
    T1[1][1] = Fo*np.cos(delta) 
    T1[1][2] = (1/2)*np.sin(delta)*(-No+Ne)/(No*Fe) 
    T1[1][3] = -(1/2)*Fe*np.sin(delta)*(No+Ne)/No

    T1[2][0] = (1/2)*np.sin(delta)*(No+Ne)/(Ne*Fo) 
    T1[2][1] = (1/2)*Fo*np.sin(delta)*(-No+Ne)/Ne 
    T1[2][2] = np.cos(delta)/Fe 
    T1[2][3] = 0

    T1[3][0] = (1/2)*np.sin(delta)*(-No+Ne)/(Ne*Fo) 
    T1[3][1] = (1/2)*Fo*np.sin(delta)*(No+Ne)/Ne 
    T1[3][2] = 0 
    T1[3][3] = Fe*np.cos(delta)
    
    return T1

def T2_matrix(K, pitch, Q_N_pitch2, L2, NoC, NeC):   
    
    N_pitch2 = L2 / pitch
    Q2 = Q_N_pitch2 / N_pitch2
    
    delta = 2 * np.pi / Q2
    
    Fo = np.exp(I*2*Pi*K*pitch/Q2*NoC)
    Fe = np.exp(I*2*Pi*K*pitch/Q2*NeC)
    
    No = NoC
    Ne = NeC
    
    T2 = np.zeros((4, 4))

    T2[0][0] = np.cos(delta)/Fo 
    T2[0][1] = 0
    T2[0][2] = -(1/2)*np.sin(delta)*(No+Ne)/(No*Fe)
    T2[0][3] = (1/2)*Fe*np.sin(delta)*(-No+Ne)/No

    T2[1][0] = 0
    T2[1][1] = Fo*np.cos(delta) 
    T2[1][2] = (1/2)*np.sin(delta)*(-No+Ne)/(No*Fe) 
    T2[1][3] = -(1/2)*Fe*np.sin(delta)*(No+Ne)/No

    T2[2][0] = (1/2)*np.sin(delta)*(No+Ne)/(Ne*Fo) 
    T2[2][1] = (1/2)*Fo*np.sin(delta)*(-No+Ne)/Ne 
    T2[2][2] = np.cos(delta)/Fe 
    T2[2][3] = 0

    T2[3][0] = (1/2)*np.sin(delta)*(-No+Ne)/(Ne*Fo) 
    T2[3][1] = (1/2)*Fo*np.sin(delta)*(No+Ne)/Ne 
    T2[3][2] = 0 
    T2[3][3] = Fe*np.cos(delta)
    
    return T2

def Tdf_matrix(K, Ld, Nd, NoC, NeC):
    delta = 0
    
    FeD = np.exp(I*2*Pi*K*Ld*Nd)
    Fo = FeD
    Fe = FeD
    
    N0 = (NoC + NeC) / 2
    
    No = N0
    Ne = N0
    
    TD = np.zeros((4, 4))

    TD[0][0] = np.cos(delta)/Fo 
    TD[0][1] = 0
    TD[0][2] = -(1/2)*np.sin(delta)*(No+Ne)/(No*Fe)
    TD[0][3] = (1/2)*Fe*np.sin(delta)*(-No+Ne)/No

    TD[1][0] = 0
    TD[1][1] = Fo*np.cos(delta) 
    TD[1][2] = (1/2)*np.sin(delta)*(-No+Ne)/(No*Fe) 
    TD[1][3] = -(1/2)*Fe*np.sin(delta)*(No+Ne)/No

    TD[2][0] = (1/2)*np.sin(delta)*(No+Ne)/(Ne*Fo) 
    TD[2][1] = (1/2)*Fo*np.sin(delta)*(-No+Ne)/Ne 
    TD[2][2] = np.cos(delta)/Fe 
    TD[2][3] = 0

    TD[3][0] = (1/2)*np.sin(delta)*(-No+Ne)/(Ne*Fo) 
    TD[3][1] = (1/2)*Fo*np.sin(delta)*(No+Ne)/Ne 
    TD[3][2] = 0 
    TD[3][3] = Fe*np.cos(delta)
    
    return TD

    
'''
На подумать, можно ли сделать красиво и правильно,
используя только одну функцию T для T1 T2, а, соответсвенно,
и для Fo, Fe и т.д. 

def F(K, pitch, Q_N_pitch, L, N):
    
    F = np.exp(I*2*Pi*K*pitch/(Q_N_pitch*pitch/L)*N)

def T_matrix(delta, No, Ne):
    
    Fo = F()
    
    T = np.zeros((4, 4))
    
    T[0][0] = (np.cos(delta))/Fo
    T[0][1] = 0
    T[0][2] = -((No+Ne)*np.sin(delta))/(2*No*Fe)
    T[0][3] = (Fe*(Ne-No)*np.sin(delta))/(2*No)

    T[1][0] = 0
    T[1][1] = Fo*np.cos(delta)
    T[1][2] = ((Ne-No)*np.sin(delta))/(2*No*Fe)
    T[1][3] = -(Fe*(No+Ne)*np.sin(delta))/(2*No)

    T[2][0] = ((No+Ne)*np.sin(delta))/(2*Ne*Fo) 
    T[2][1] = (Fo*(Ne-No)*np.sin(delta))/(2*Ne)
    T[2][2] = (np.cos(delta))/Fe
    T[2][3] = 0

    T[3][0] = ((Ne-No)*np.sin(delta))/(2*Ne*Fo)
    T[3][1] = (Fo*(No+Ne)*np.sin(delta))/(2*Ne)
    T[3][2] = 0
    T[3][3] = Fe*np.cos(delta)
'''
