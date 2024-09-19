import numpy as np
import matplotlib.pyplot as plt

from calc import calculate_TO, calculate_OT, Omega

#lmbd = (2 *  np.pi / Omega) * 1000

TOY = calculate_TO ()
OTY = calculate_OT ()

plt.scatter (Omega, TOY, s = 15)
plt.scatter (Omega, OTY, s = 2)

plt.show()