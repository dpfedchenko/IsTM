import numpy as np
from numpy import cos, sin, exp, diag, matrix

# Constants
from assign import Pi, I

# Functions
def F(K, Q, N, pitch):
    return exp(I * 2 * Pi * K * pitch/2/Q * N)
def FeD(K, Ld, N0):
    return exp(I * 2 * Pi * K * Ld/2 * N0)

# Matrix
def Pr(K, Q, Ne, No, pitch):
    Fo = F (K, Q, No, pitch)
    Fe = F (K, Q, Ne, pitch)
    return diag([Fo**-1, Fo, Fe**-1, Fe])

def Dm(No, Ne):
    return matrix ([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def Di(No, Ne):
    return Dm (No, Ne)**-1

def R1m(phi):
    C, S = cos(phi), sin(phi)
    return matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def R2i(phi2):
    C, S = cos(phi2), sin(phi2)
    return R1m (phi2)**-1

def _calculate_T_matrix(delta, Fo, Fe, No, Ne):
    S = sin(delta)
    C = cos(delta)
    return np.matrix([
      [C / Fo**2, 0, -.5 * (S * (No + Ne)) / (Fo * Fe * No), .5 * (Fe * S * (-No + Ne)) / (Fo * No)],
      [0, Fo**2 * C, .5 * (Fo * S * (-No + Ne)) / (Fe * No), -.5 * Fo * Fe * S * (No + Ne) / No],
      [.5 * (S * (No + Ne)) / (Fe * Ne * Fo), .5 * (Fo * S * (-No + Ne)) / (Fe * Ne), C / Fe**2, 0],
      [.5 * (Fe * S * (-No + Ne)) / (Ne * Fo), .5 * (Fo * Fe * S * (No + Ne)) / Ne, 0, Fe**2 * C]
    ])

def T1(delta, K, Q, Ne, No, pitch):
    Fo = F(K, Q, No, pitch)
    Fe = F(K, Q, Ne, pitch)
    return _calculate_T_matrix(delta, Fo, Fe, No, Ne)

def T2(delta, K, Ld, N0):
    Fo = FeD(K, Ld, N0)
    Fe = Fo
    return _calculate_T_matrix(delta, Fo, Fe, N0, N0)