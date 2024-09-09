import matplotlib.pyplot as plt
from matrix import Forward, Back, Omega, define_difference

forwardY = Forward()
BackY = Back()

plt.scatter(Omega, forwardY)
plt.scatter(Omega, BackY)
plt.grid()
plt.show()

define_difference(forwardY, BackY, Omega)

