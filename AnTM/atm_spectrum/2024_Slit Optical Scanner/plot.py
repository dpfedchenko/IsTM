import matplotlib.pyplot as plt
import numpy as np

from build import rotate, sclr_prod # type: ignore
from calc import midx, midy # type: ignore

def spectrum_plot():
    fig, ax = plt.subplots()
    # spectrum_values = [np.pi/5.5, np.pi/7.5, np.pi/11.5, np.pi/21.5, 0, -np.pi/5.5, -np.pi/7.5, -np.pi/11.5, -np.pi/21.5]
    spectrum_values = [360/5.5, 360/7.5, 360/11.5, 360/21.5, 0, -360/5.5, -360/7.5, -360/11.5, -360/21.5]
    sorted_spectrum_values = sorted(spectrum_values)
    index = np.arange(0, len(sorted_spectrum_values))
    ax.scatter(index, sorted_spectrum_values)


def plot_system(angle, initial_angle, x0, y0, N, hx, hy, r, rotation_angle, pairs):
    
    fig, ax = plt.subplots()

    rhx = rotate(0, 0, hx, 0, rotation_angle)
    rhy = rotate(0, 0, 0, hy, rotation_angle)

    ax.scatter(midx, midy, c='black', s=.8)
    ax.plot([0, rhx[0]], [0, rhx[1]], c='black')
    ax.plot([0, rhy[0]], [0, rhy[1]], c='black')

    for i in range(len(pairs)):
        rot_pair = rotate(midx, midy, pairs[i][0], pairs[i][1], rotation_angle)
        ax.scatter(rot_pair[0], rot_pair[1], c='r', s=30)

    scpr = []
    for i in range(N + 1):
        rayx = np.exp(1j * (initial_angle + angle * i/N)).real
        rayy = np.exp(1j * (initial_angle + angle * i/N)).imag
        scpr.append(abs(sclr_prod(rhx, [rayx, rayy])))

    min_index = np.argmin(np.array(scpr))

    for i in range(N + 1):
        ax.plot([x0, r * np.exp(1j * (initial_angle + angle * i/N)).real],
                [y0, r * np.exp(1j * (initial_angle + angle * i/N)).imag], c='b', linewidth=.5)
        
        if i == min_index:
            ax.plot([x0, r * np.exp(1j * (initial_angle + angle * i/N)).real],
                    [y0, r * np.exp(1j * (initial_angle + angle * i/N)).imag], c='g', linewidth=2)