from numpy import pi, cos, sin, exp, diag, matrix

def F(K, Q, N, pitch):
    return exp(1j * 2 * pi * K * pitch/2/Q * N)

def FeD(K, Ld, Nd):
    return exp(1j * 2 * pi * K * Ld/2 * Nd)

def Pr(K, Q, Ne, No, pitch):
    Fo = F (K, Q, No, pitch)
    Fe = F (K, Q, Ne, pitch)
    return diag([Fo**-1, Fo, Fe**-1, Fe])

def Dm(No, Ne):
    return matrix ([[1, 1, 0, 0], [No, -No, 0, 0], [0, 0, 1, 1], [0, 0, Ne, -Ne]])

def R1m(phi):
    C, S = cos(phi), sin(phi)
    return matrix([[C, 0, S, 0], [0, C, 0, S], [-S, 0, C, 0], [0, -S, 0, C]])

def _calculate_T_matrix(delta, Fo, Fe, No, Ne):
    S, C = sin(delta), cos(delta)
    return matrix([
      [C / Fo**2, 0, -.5 * (S * (No + Ne)) / (Fo * Fe * No), .5 * (Fe * S * (-No + Ne)) / (Fo * No)],
      [0, Fo**2 * C, .5 * (Fo * S * (-No + Ne)) / (Fe * No), -.5 * Fo * Fe * S * (No + Ne) / No],
      [.5 * (S * (No + Ne)) / (Fe * Ne * Fo), .5 * (Fo * S * (-No + Ne)) / (Fe * Ne), C / Fe**2, 0],
      [.5 * (Fe * S * (-No + Ne)) / (Ne * Fo), .5 * (Fo * Fe * S * (No + Ne)) / Ne, 0, Fe**2 * C]
    ])

def T(delta, K, Q, Ne, No, pitch):
    Fo = F(K, Q, No, pitch)
    Fe = F(K, Q, Ne, pitch)
    return _calculate_T_matrix(delta, Fo, Fe, No, Ne)

def Td(delta, K, Ld, Nd):
    Fo = FeD(K, Ld, Nd)
    Fe = Fo
    return _calculate_T_matrix(delta, Fo, Fe, Nd, Nd)