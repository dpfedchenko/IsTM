import numpy as np
import random

NK = 200
N_sub = 25
KR = [1/0.700, 1/0.500]

layer0 = [1.71, 1.71, 1.70, 1.71, 1.65, 1.69, 1.67, 1.63, 1.70, 1.69, 1.71, 1.63, 1.70, 1.71, 1.67, 1.69, 1.69, 1.71, 1.70, 1.69, 1.71, 1.65, 1.70, 1.71, 1.67, 1.69, 1.62, 1.70, 1.70, 1.69]
num_lists = 3
min_correction = -0.26
max_correction = +0.26

perturb_layers = []
for _ in range(num_lists):
    new_list = [x + random.uniform(min_correction, max_correction) for x in layer0]
    layers = []
    for i in range(len(layer0)):
        layers.append([0.5, new_list[i], 1.496, 1/0.320, 0])
    perturb_layers.append(layers)