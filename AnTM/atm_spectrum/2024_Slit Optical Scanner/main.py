import matplotlib.pyplot as plt

from assign import angle, initial_angle, x0, y0, N, hx, hy, r, rotation_angle # type: ignore
from build import rotate # type: ignore
from calc import pairs # type: ignore
from plot import plot_system, spectrum_plot # type: ignore

plot_system(angle, initial_angle, x0, y0, N, hx, hy, r, rotation_angle, pairs)
# spectrum_plot()

#plt.axis('equal')
#plt.xlim(-1, 1)
#plt.ylim(-.5, 2.5)
plt.show()