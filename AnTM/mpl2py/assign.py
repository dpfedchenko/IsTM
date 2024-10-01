from numpy import arange
NK = 1000
KR = [1/.8, 1/.560]
t = arange(0, NK + 1, 1)
lmbd = 1000 / (KR[0] + (KR[1] - KR[0]) * t / NK)
pitch = .4533
Ne = 1.57
No = 1.42
N0 = (Ne + No) / 2
Nd = 1.42 + .0075j
Ld = .1197