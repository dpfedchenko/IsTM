import numpy as np
from numpy import ones, array
import math
from IsTM_matrix import Pr, iPr, D, iD
def goTM(SL, Nsub, Out, Kg):
    ng, Tg, zg, Nl = [], [], [0], len(SL)
    for i in range(Nl): ng += (SL[i][0] * ones(Nsub)).tolist()
    for i in range(Nl):
        for j in range(Nsub): zg.append(zg[-1] + SL[i][1] * math.ceil(j/Nsub)/(Nsub - 1))
    zg = zg[1:len(zg)]
    Lzg, dzg = len(zg), np.diff(array(zg))
    for k in Kg:
        E = [[0, 0]]*Lzg
        E[-1] = Out
        for j in range(Lzg - 2, -1, -1):
            Prj, iPrj, Dj, iDj = Pr(k, ng[j], dzg[j]), iPr(k, ng[j], dzg[j]), D(ng[j + 1]), iD(ng[j])
            if dzg[j]: E[j] = iPrj @ E[j + 1]
            else: E[j] = iDj @ Dj @ E[j + 1]
        if len(Kg) == 1: break
        else: Tg.append(abs(E[-1][0]/E[0][0])**2)
    return [zg, E, Tg, ng]