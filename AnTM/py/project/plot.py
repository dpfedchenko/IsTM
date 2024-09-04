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
  
def plot_diff_Tw(x, y):
  dy = np.diff(y)
  dx = np.diff(x)
  dy_dx = dy / dx
  
  x_derivative = x[:-1]
  normalize_dy_dx = dy_dx / (max(dy_dx) - min(dy_dx))
  
  plt.figure(figsize=(10,6))
  plt.plot(x, y, label='T(w)')
  plt.plot(x_derivative, normalize_dy_dx + abs(min(normalize_dy_dx)), color='orange', label='dT(w)/dw')
 
  yderiv0 = [abs(min(normalize_dy_dx))] * len(x)
  y05 = [0.5] * len(x)
  
  plt.plot(x, y05, color='red')
  plt.plot(x, yderiv0, color='black')
  
  '''
  y1 = [1] * len(x)
  y0 = [0] * len(x)
  plt.plot(x, y1, color='black', linestyle='--')
  plt.plot(x, y05, color='black', linestyle='--')
  plt.plot(x, y0, color='black', linestyle='--')
  '''
  plt.grid()
  #plt.tight_layout()
  plt.show()
  
  