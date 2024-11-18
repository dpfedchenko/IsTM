import numpy as np
import Parameters, Matrices
   
RmL1 = Matrices.R1m_matrix(
    Parameters.Lzero_RmL1,
    Parameters.pitch
)

RmL2 = Matrices.R1m_matrix(
    Parameters.Lzero_RmL2,
    Parameters.pitch
)

RiR1 = Matrices.R2i_matrix(
    Parameters.L1,
    Parameters.pitch
)

RiR2 = Matrices.R2i_matrix(
    Parameters.L2,
    Parameters.pitch
)

DmC = Matrices.Dm_matrix(
    Parameters.NoC, 
    Parameters.NeC
)

DiC = Matrices.Di_matrix(
    Parameters.NoC, 
    Parameters.NeC
)

TL = Matrices.Di_matrix(
    Parameters.N0,
    Parameters.N0
)

TR = Matrices.Dm_matrix(
    Parameters.N0,
    Parameters.N0
)


K20 = 1 / 0.9
K2 = 1/0.4
K_steps = 500
K_values = np.linspace(K20, K2, K_steps+1)

for K in K_values:
    T1 = Matrices.T1_matrix(
        K, 
        Parameters.pitch, 
        Parameters.Q_N_pitch1,
        Parameters.L1,
        Parameters.NoC1,
        Parameters.NeC1
    )
    
    T2 = Matrices.T2_matrix(
        K, 
        Parameters.pitch, 
        Parameters.Q_N_pitch2,
        Parameters.L2,
        Parameters.NoC2,
        Parameters.NeC2
    )
    
    Tdf = Matrices.Tdf_matrix(
        K,
        Parameters.Ld,
        Parameters.Nd,
        Parameters.NoC,
        Parameters.NeC
    )
    
    TCLC1 = RmL1 @ DmC @ (T1**Parameters.Q_N_pitch1) @ DiC @ RiR1
    TCLC2 = RmL2 @ DmC @ (T2**Parameters.Q_N_pitch2) @ DiC @ RiR2
    TDef = RmL1 @ DmC @ Tdf @ DiC @ RiR2
    
    TT = TL @ TCLC1 @ TDef @ TCLC2 @ TR
    
    K1 = np.array([
        TT[0, 0],
        0,
        TT[1, 1],
        0
    ])
    
    Eq1 = K1[0] - 1/np.sqrt(2)
    Eq2 = K1[1] - 
    Eq3 = K1[0] - 1/np.sqrt(2)
    Eq4 = K1[0] - 1/np.sqrt(2)
    
    
    
    