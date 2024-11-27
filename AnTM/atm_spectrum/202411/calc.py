import numpy as np

from assign import NK, N_sub, KR, LR_def, LR_CLC1, LR_CLC2

from build import P, Dm, Di, R1m, R2i, calculate_transmittance
from build import delta_CLC1, RmL_CLC1, RiR_CLC1, Dm_CLC1, Di_CLC1
from build import delta_CLC2, RmL_CLC2, RiR_CLC2, Dm_CLC2, Di_CLC2
from build import RmL_def, RiR_def, Dm_def, Di_def
from build import TL, TR

def TA_spectrum_calc():
    T, A, R = [], [], []
    for i in range(NK + 1):
        K = KR[0] + i * (KR[1] - KR[0]) / NK
        
        Fe_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC1[0] / N_sub / 2 * LR_CLC1[1])
        Fo_CLC1 = np.exp(1j * 2 * np.pi * K * LR_CLC1[0] / N_sub / 2 * LR_CLC1[2])
        
        Tf_CLC1 = P(Fo_CLC1, Fe_CLC1) @\
             Di(LR_CLC1[2], LR_CLC1[1]) @\
                 R2i(LR_CLC1[4] + delta_CLC1) @\
                     R1m(LR_CLC1[4]) @ Dm(LR_CLC1[2], LR_CLC1[1]) @\
                         P(Fe_CLC1, Fo_CLC1)
        
        Fe_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[1])
        Fo_CLC2 = np.exp(1j * 2 * np.pi * K * LR_CLC2[0] / N_sub / 2 * LR_CLC2[2])
        
        Tf_CLC2 = P(Fo_CLC2, Fe_CLC2) @\
             Di(LR_CLC2[2], LR_CLC2[1]) @\
                 R2i(LR_CLC2[4] + delta_CLC2) @\
                     R1m(LR_CLC2[4]) @ Dm(LR_CLC2[2], LR_CLC2[1]) @\
                         P(Fe_CLC2, Fo_CLC2)
        
        FeD = np.exp(1j * 2 * np.pi * K * LR_def[0] / 2 * LR_def[1])
        Tf_def = P(FeD, FeD) @ Di(LR_def[1], LR_def[1]) @ R2i(0) @ R1m(0) @ Dm(LR_def[1], LR_def[1]) @ P(FeD, FeD)
        
        TCLC1 = RmL_CLC1 @ Dm_CLC1 @ np.linalg.matrix_power(Tf_CLC1, N_sub) @ Di_CLC1 @ RiR_CLC1
        TCLC2 = RmL_CLC2 @ Dm_CLC2 @ np.linalg.matrix_power(Tf_CLC2, N_sub) @ Di_CLC2 @ RiR_CLC2
        TDef = RmL_def @ Dm_def @ Tf_def @ Di_def @ RiR_def

        TT = TCLC1 @ TDef @ TCLC2
        TT = TL @ TT @ TR
        tx = calculate_transmittance(TT)[0]
        ty = calculate_transmittance(TT)[1]
        rx = calculate_transmittance(TT)[2]
        ry = calculate_transmittance(TT)[3]
        T.append(abs(tx)**2 + abs(ty)**2)
        R.append(abs(rx)**2 + abs(ry)**2)
        A.append(1 - T[-1] - R[-1])
    return [T, A, R]