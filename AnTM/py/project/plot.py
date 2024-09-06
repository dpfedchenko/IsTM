import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from numpy import pi

def plot_transmission_spectra(x, y):
  plt.figure(figsize=(10,6))
  plt.plot(x, y)
  plt.grid()
  plt.ylim(-0.1, 1.1)
  plt.show()
  
def plot_transmission_spectra_OxWaveLength(x, y):
  
  lyambda = (2 *  pi / x) * 1000 
  #lyambda = (x/(2 * pi)) * 1000 
  
  plt.figure(figsize=(10,6))
  plt.plot(lyambda, y)
  plt.grid()
  plt.ylim(-0.1, 1.1)
  plt.show()

def plot_TD (x, y, ledge, redge, Tcolor):
  
  fig, ax = plt.subplots()
  lyambda = (2 *  pi / x) * 1000 
  ax.plot(lyambda, y, color = Tcolor)
  ax.grid()
  
  ax.set_xlim (ledge, redge)
  ax.set_ylim (0, 1.1)
  
  ax.set_xlabel ('Wavelength, nm')
  ax.set_ylabel ('Transmittance')

  plt.show()

def double_plot_TD (x, y1, y2, diff, ledge, redge, Tcolor1, Tcolor2):
  
  fig, (ax1, ax) = plt.subplots(2, 1)
  lyambda = (2 *  pi / x) * 1000

  ax1.plot(lyambda, y1, color = Tcolor1, label = 'CLC32')
  ax1.plot(lyambda, y2, color = Tcolor2, label = 'CLC23')
  ax1.plot([677.904, 677.904], [0.5, 0.7], color = 'gray')
  ax1.set_xlim (677, 679)
  ax1.set_ylim (0.5, 0.7)
  ax1.set_ylabel ('Transmittance')

  ax.plot(lyambda, y1, color = Tcolor1, label = 'CLC32')
  ax.plot(lyambda, y2, color = Tcolor2, label = 'CLC23')
  ax.plot(lyambda, diff, color = 'green', label = 'Diff')
  
  ax.plot(np.array(lyambda), np.array(y1) - np.array(y2), color = 'magenta')
  ax.plot([677.904, 677.904], [-0.1, 1], color = 'gray')
  ax.grid()
  
  ax.set_xlim (ledge, redge)
  ax.set_ylim (-0.1, 1.1)
  
  ax.set_xlabel ('Wavelength, nm')
  ax.set_ylabel ('Transmittance')
  
  fig.savefig('CLC.png', format = 'png', dpi = 500)

  plt.legend()
  plt.show()


def plot3d_TwLo(x, y, z):
  fig, ax = plt.subplot()
  ax.plot_wireframe(x, y, z, rstride = 1, cstride = 1)
  plt.show()
  
  