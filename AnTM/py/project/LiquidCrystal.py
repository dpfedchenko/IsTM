import numpy as np

epsilon_o = 2.56
mu_o = 1
epsilon_e = 3.24
mu_e = 1

No = np.sqrt(epsilon_o * mu_o)
Ne = np.sqrt(epsilon_e * mu_e)

xi = (mu_e * No) / (mu_o * Ne)
_xi = 1 / xi

X_M = xi + _xi

# Шаг спирали 
Lo = 1

L = 5

Matrix = [
  [0, 0, 0, 0],
  [0, 0, 0, 0], 
  [0, 0, 0, 0],
  [0, 0, 0, 0]
  ]