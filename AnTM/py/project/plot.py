import matplotlib.pyplot as plt

def plot_transmission_spectra(x, y):
  plt.plot(x, y)
  plt.grid()
  plt.ylim(0.05, 1.05)
  plt.show()