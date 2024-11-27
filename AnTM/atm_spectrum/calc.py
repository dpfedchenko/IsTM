import numpy as np
from assign import NK, N_sub, KR, layers
from build import P, Dm, Di, R1m, R2i, calculate_transmittance, create_layer_matrices

LR_sub = [np.sqrt( layers[0]['Ne'] * layers[0]['No'])]
TL = Di(LR_sub[0], LR_sub[0])
TR = Dm(LR_sub[0], LR_sub[0])
lmbd = 1000 / (KR[0] + (KR[1] - KR[0]) * np.arange(0, NK + 1, 1) / NK)

def TA_spectrum_calc():
    T, A, R = [], [], []
    for i in range(NK + 1):
        K = KR[0] + i * (KR[1] - KR[0]) / NK
        total_transfer_matrix = TL

        for layer in layers:
            delta, RmL, RiR, Dm_layer, Di_layer = create_layer_matrices(layer)

            if layer['name'] == 'CLC1' or layer['name'] == 'CLC2':
                Fe = np.exp(1j * 2 * np.pi * K * layer['L'] / N_sub / 2 * layer['Ne'])
                Fo = np.exp(1j * 2 * np.pi * K * layer['L'] / N_sub / 2 * layer['No'])
                Tf = P(Fo, Fe) @ Di_layer @ RiR @ RmL @ Dm_layer @ P(Fe, Fo)
                Tlayer = RmL @ Dm_layer @ np.linalg.matrix_power(Tf, N_sub) @ Di_layer @ RiR
            elif layer['name'] == 'Defect':
                FeD = np.exp(1j * 2 * np.pi * K * layer['param1'] / 2 * layer['param2'])
                Tf_def = P(FeD, FeD) @ Di_layer @ RiR @ RmL @ Dm_layer @ P(FeD, FeD)
                Tlayer = RmL @ Dm_layer @ Tf_def @ Di_layer @ RiR
            else:
                raise ValueError(f"Unknown layer type: {layer['name']}")
            total_transfer_matrix = total_transfer_matrix @ Tlayer

        total_transfer_matrix = total_transfer_matrix @ TR
        tx, ty, rx, ry = calculate_transmittance(total_transfer_matrix)
        T.append(abs(tx)**2 + abs(ty)**2)
        R.append(abs(rx)**2 + abs(ry)**2)
        A.append(1 - T[-1] - R[-1])
    return T, A, R