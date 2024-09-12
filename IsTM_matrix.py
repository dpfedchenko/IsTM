from scipy.linalg import expm
from numpy import diag, array, pi
I = complex(0, 1)
def Pr  (k, ng, dzg): return (expm(diag(array([1, -1]) * 2 * I * pi * k * ng * dzg)))      
def iPr (k, ng, dzg): return (expm(diag(array([-1, 1]) * 2 * I * pi * k * ng * dzg)))
def D  (ng): return array([[1, 1], [ng, -ng]])
def iD (ng): return array([[ng, 1], [ng, -1]]) * 1/(2 * ng)