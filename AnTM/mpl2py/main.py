import numpy as np
import matplotlib.pyplot as plt

from calc import TO, OT, TOOT, Omega

#lmbd = (2 *  np.pi / Omega) * 1000

TOY = TO ()
OTY = OT ()
TOOT (TOY, OTY, Omega)

plt.scatter (Omega, TOY, s = 15)
plt.scatter (Omega, OTY, s = 2)

#plt.grid()
plt.show()
