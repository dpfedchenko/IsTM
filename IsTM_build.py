import math
from numpy import array, repeat

def build_ng(SL, Nsub):
  ng = array([val for val, _ in SL])
  ng = repeat(ng, Nsub)
  return ng

def build_zg(SL, Nsub):
  zg = [0]
  for i in range(len(SL)):
    for j in range(Nsub):
      zg.append(zg[-1] + SL[i][1] * math.ceil(j / Nsub) / (Nsub - 1))
  return zg[1:]