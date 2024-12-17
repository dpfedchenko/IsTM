import numpy as np

def sclr_prod(x, y):
    return x[0]*y[0] + x[1]*y[1]

def rotate(x0, y0, x, y, phi):
    return np.cos(phi) * (x - x0) - np.sin(phi) * (y - y0) + x0, np.sin(phi) * (x - x0) + np.cos(phi) * (y - y0) + y0