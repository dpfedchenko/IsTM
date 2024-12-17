import numpy as np
from assign import NK, N_sub, KR, perturb_layers
from build import calculate_transmittance, clc_layer, layer_parameters
from build import TL, TR

def TA_spectrum_calc():
    players = []
    for p in range(len(perturb_layers)):
        layers = perturb_layers[p]
        T, A, R = [], [], []
        for i in range(NK + 1):
            K = KR[0] + i * (KR[1] - KR[0]) / NK
            Structure = []
            TCLC = np.eye(4)
            for j in range(len(layers)):
                delta, RmL, RiR, DmM, DiM = layer_parameters(layers[j])
                Tf_CLC = clc_layer(K, layers[j], delta)
                Structure.append(RmL @ DmM @ np.linalg.matrix_power(Tf_CLC, N_sub) @ DiM @ RiR)
                TCLC = TCLC @ Structure[-1]
            TT = TL @ TCLC @ TR
            tx, ty = calculate_transmittance(TT)[0], calculate_transmittance(TT)[1]
            rx, ry = calculate_transmittance(TT)[2], calculate_transmittance(TT)[3]
            T.append(abs(tx)**2 + abs(ty)**2)
            R.append(abs(rx)**2 + abs(ry)**2)
            A.append(1 - T[-1] - R[-1])
        players.append([T, A, R])
    return players