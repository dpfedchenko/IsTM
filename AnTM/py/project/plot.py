import matplotlib.pyplot as plt
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

def plot3d_TwLo(x, y, z):
  fig, ax = plt.subplot()
  ax.plot_wireframe(x, y, z, rstride = 1, cstride = 1)
  plt.show()
  
  