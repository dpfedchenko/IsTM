from scipy.linalg import expm
from numpy import array, diff, diag, pi
from IsTM_matrix import Pr, iPr, D, iD
from IsTM_build import build_ng, build_zg

def acalculate_TM(SL):
  resP = array([[1, 0], [0, 1]])
  for i in range(len(SL) - 1):
    resP = expm(diag(array([+1, -1]) * 2 * 1j * pi * SL[i][0] * SL[i][1])) @ resP
  resP = D(SL[0][0]) @ resP @ D(SL[-1][0])
  return resP

def calculate_E(Lzg, dzg, ng, Out, k):
  E = [[0, 0]] * Lzg
  E[-1] = Out
  for j in range(Lzg - 2, -1, -1):
    Prj, iPrj, Dj, iDj = Pr(k, ng[j], dzg[j]), iPr(k, ng[j], dzg[j]), D(ng[j + 1]), iD(ng[j])
    if dzg[j]:
      E[j] = iPrj @ E[j + 1]
    else:
      E[j] = iDj @ Dj @ E[j + 1]
  return E

def calculate_TM(SL, Nsub, Out, Kg):
  ng = build_ng(SL, Nsub)
  zg = build_zg(SL, Nsub)
  Lzg = len(zg)
  dzg = diff(array(zg))
  Tg = []
  for k in Kg:
    E = calculate_E(Lzg, dzg, ng, Out, k)
    if len(Kg) == 1:
      break
    else:
      Tg.append (abs(E[-1][0] / E[0][0])**2)
  return [zg, E, Tg, ng]