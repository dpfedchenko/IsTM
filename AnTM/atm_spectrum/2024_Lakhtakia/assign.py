import numpy as np
import random
import statistics as st

NK = 200
N_sub = 25
KR = np.array([1/0.700, 1/0.500])

initial_layers = np.array([1.72]*30)
illen = len(initial_layers)

num_lists = 10
corrections = [0, 0.3]
perturb_layers = []
for r in range(len(corrections)):
    trials = []
    for _ in range(num_lists):
        noise = np.random.uniform(-corrections[r], corrections[r], size=illen)
        new_list = initial_layers + noise
        trials.append(new_list)
    everage_curve = np.mean(np.array(trials), axis=0)
    layers = np.column_stack((np.full(illen, 0.495),
                                        everage_curve,
                                        np.full(illen, 1.51),
                                        np.full(illen, 1/0.320),
                                        np.zeros(illen)))
    perturb_layers.append(layers)