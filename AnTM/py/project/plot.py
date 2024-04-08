import matplotlib.pyplot as plt

def plot_transmission_spectra(omega_x, TC):
    plt.plot(omega_x, TC)
    plt.grid()
    plt.show()