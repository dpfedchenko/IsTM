import matplotlib.pyplot as plt

def plot_transmission_spectra(x, y):
  plt.plot(x, y)
  plt.grid()
  plt.ylim(-0.1, 1.1)
  plt.show()