# Python libraries
import numpy as np
import math

# TM modules
import IsTM_matrix as ITMm

# TMB_go
def goTM(SL, Nsub, Out, Kg):
    ng, zg = [], [0]
    Nl = len(SL)
    for i in range(Nl):
        ng += (SL[i][0] * np.ones(Nsub)).tolist()
    for i in range(Nl):
        for j in range(Nsub):
            zg.append(zg[-1] + SL[i][1] * math.ceil(j/Nsub)/(Nsub - 1))
    zg = zg[1:len(zg)]
    dzg = np.diff(np.array(zg))
    Tg, E = [], []
    
    # TMC
    for k in Kg:
        for i in range(len(zg)):
            E.append([0, 0])
        E[-1] = Out
        for j in range(len(zg) - 2, -1, -1):
            if dzg[j]:
                E[j] = ITMm.iPr(k, ng[j], dzg[j], E[j + 1])
            else:
                E[j] = (ITMm.iD(ng[j]) @\
                        ITMm.D(ng[j + 1]) @\
                        np.array(E[j + 1])).tolist()
        if len(Kg) == 1:
            rAg, rBg, aAg, aBg, pAg, pBg = [], [], [], [], [], []
            for i in range(len(E)):
                rAg.append(E[i][0].real)
                rBg.append(E[i][1].real) 
                aAg.append(abs(E[i][0]))
                aBg.append(abs(E[i][1]))
        else:
            Tg.append(abs(E[-1][0]/E[0][0])**2)
    return [zg, E, Tg, ng]