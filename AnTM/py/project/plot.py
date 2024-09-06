import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def plot_transmission_spectra(x, y):
  plt.figure(figsize=(10,6))
  plt.plot(x, y)
  plt.grid()
  plt.ylim(-0.1, 1.1)
  plt.show()
  
def plot_transmission_spectra_OxWaveLength(x, y):
  
  lyambda = (2 *  np.pi / x) * 1000 
  #lyambda = (x/(2 * pi)) * 1000 
  
  plt.figure(figsize=(10,6))
  plt.plot(lyambda, y)
  plt.grid()
  plt.ylim(-0.1, 1.1)
  plt.show()

def plot3d_TwLo(x, y, z):
  fig, ax = plt.subplot()
  ax.plot_wireframe(x, y, z, rstride = 1, cstride = 1)
  plt.show()

def plot_TC_dTC(x, y, derivative):
  
  dx, dy_dx, dy_dx0 = derivative
  dy_dx0 = [dy_dx0] * len(x)
  
  plt.figure(figsize=(10,6))
  
  plt.plot(x, y, label='T(w)')
  plt.plot(dx, dy_dx, label='dT(w)/dw', color='orange', alpha=0.7)
  plt.plot(x, dy_dx0, color='orange', label='y`= 0', linewidth=0.8)
  
  plt.scatter([dx[np.argmax(dy_dx)], dx[np.argmin(dy_dx)]], [max(dy_dx), min(dy_dx)], color='darkorange')
  
  plt.yticks(np.arange(0, 1.25, 0.25))
  plt.grid()
  plt.show()
  
  
  
  