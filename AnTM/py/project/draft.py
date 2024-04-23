import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

Los = [1, 2, 3]

for Lo_value in Los:
    omega_x = np.linspace(-10, 10, 1000)
    Y = [Lo_value]*len(omega_x)
    TC = np.sin(omega_x)
    
    ax.scatter(omega_x, Y, TC)

plt.show()