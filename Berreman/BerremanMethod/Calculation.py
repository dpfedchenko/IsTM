import numpy as np
import Matrices, Parameters

RmL1 = Matrices.R1m_matrix(
    Parameters.phi_L1
)

RmL2 = Matrices.R1m_matrix(
    Parameters.phi_L
)

RiR1 = Matrices.R2i_matrix(
    Parameters.phi_R1
)

RiR2 = Matrices.R2i_matrix(
    Parameters.phi_R2
)

DmC = Matrices.Dm_matrix(
    Parameters.NoC, 
    Parameters.NeC
)

DiC = Matrices.Di_matrix(
    Parameters.NoC, 
    Parameters.NeC
)

T1 = Matrices.T1_matrix(
    Parameters.K, 
    Parameters.pitch, 
    Parameters.Q_N_pitch1,
    Parameters.L1,
    Parameters.NoC,
    Parameters.NeC
)

T2 = Matrices.T2_matrix(
    Parameters.K, 
    Parameters.pitch, 
    Parameters.Q_N_pitch2,
    Parameters.L2,
    Parameters.NoC,
    Parameters.NeC
)

TD = Matrices.Tdf_matrix(
    Parameters.K,
    Parameters.Ld,
    Parameters.Nd,
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


'''
T1 = Matrices.T_matrix(Parameters.delta, )
'''

