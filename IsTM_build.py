from numpy import array, repeat, cumsum, ceil, arange

def build_ng(SL, Nsub):
  ng = array([val for val, _ in SL])
  ng = repeat(ng, Nsub)
  return ng

def build_zg(SL, Nsub):
  zg = [0]
  layers = array([step for _, step in SL])
  zg = cumsum(repeat(layers, Nsub) * ceil(arange(Nsub) / Nsub) / (Nsub - 1))
  return zg