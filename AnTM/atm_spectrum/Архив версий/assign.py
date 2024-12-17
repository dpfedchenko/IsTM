import numpy as np
NK = 300
N_sub = 300
KR = [1/0.750, 1/0.650]

layers = [
    {'name': 'CLC1', 'L': 3, 'Ne': 1.57, 'No': 1.4215, 'pitch': 0.454, 'phiL': 0},
    {'name': 'Defect', 'param1': 0.1197, 'param2': 1.4215 + 0.0075j, 'param3': 0, 'param4': 0, 'param5': 0},
    {'name': 'CLC2', 'L': 2, 'Ne': 1.57, 'No': 1.4215, 'pitch': 0.454, 'phiL': 0},
]
