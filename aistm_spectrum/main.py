import numpy as np
import matplotlib.pyplot as plt

SiO2 = [3, 0.25/3]
Air =  [1, 0.25]

SL = [Air, SiO2, Air]*1

def P(Exp):
  return np.diag([1/Exp, Exp])

def Dm(N):
  return np.array([[1, 1], [N, -N]])

def Di(N):
  return np.linalg.inv(Dm(N))

Nsub = 30

Tg, E = [], []
T = np.array([[1, 0], [0, 1]])
for i in range(len(SL)):
    index = len(SL) - i - 1
    for _ in range(Nsub):
        T = P(np.exp(2 * np.pi * 1j * SL[index][0] * SL[index][1] / Nsub)) @ T
        TM = T @ Dm(SL[index - 1][0]) @ Di(SL[index][0])
        E.append(TM @ np.array([1, 0]))
        Tg.append(abs(E[-1][0] / E[0][0])**2)
plt.plot(np.arange(0, len(SL) * Nsub), np.array(Tg))
plt.show()