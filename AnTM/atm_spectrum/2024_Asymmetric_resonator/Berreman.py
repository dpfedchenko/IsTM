import numpy as np
#B_wavelength = [float(item) for item in open('B_spectrum/wavelength_560_800.txt').read().split('\n')[:-1]]
#B_transmittance = [float(item) for item in open('B_spectrum/transmittance_560_800.txt').read().split('\n')[:-1]]
B32_rows = [item for item in open('B_spectrum/berreman_32.txt').read().split('\n')[::-1]]
B32_WL = [float(item.split(' ')[0]) for item in B32_rows]
B32_T = [float(item.split(' ')[1]) for item in B32_rows]
B32_R = [float(item.split(' ')[2]) for item in B32_rows]
B32_A = [float(item.split(' ')[3]) for item in B32_rows]

B23_rows = [item for item in open('B_spectrum/berreman_23.txt').read().split('\n')[::-1]]
B23_WL = [float(item.split(' ')[0]) for item in B23_rows]
B23_T = [float(item.split(' ')[1]) for item in B23_rows]
B23_R = [float(item.split(' ')[2]) for item in B23_rows]
B23_A = [float(item.split(' ')[3]) for item in B23_rows]