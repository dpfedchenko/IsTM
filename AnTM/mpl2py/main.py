import numpy as np
import matplotlib.pyplot as plt
from matrix import TO, OT, Omega, define_difference

lmbd = (2 *  np.pi / Omega) * 1000

TOY = TO ()
OTY = OT ()

plt.scatter(lmbd, TOY, s = 15)
plt.scatter(lmbd, OTY, s = 3)

plt.grid()
plt.show()

define_difference(TOY, OTY, lmbd)