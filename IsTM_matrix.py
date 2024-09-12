import numpy as np
#
I = complex(0, 1)
Pi = np.pi
   
def iPr (k, ng, dzg, E):
    '''
    return (np.diag([np.exp(-(2 * I * Pi) * k * ng * dzg),
                     np.exp( (2 * I * Pi) * k * ng * dzg)]) @\
                     np.array(E)).tolist()
    '''
    return (np.diag(np.array([-1, 1]) * np.exp(2 * I * Pi * k * ng * dzg)) @ np.array(E)).tolist()

def Pr (k, ng, dzg, E):
    return (np.diag([np.exp( (2 * I * Pi) * k * ng * dzg),
                     np.exp(-(2 * I * Pi) * k * ng * dzg)]) @\
                     np.array(E)).tolist()
        
def iD (ng):
    return np.array([[ng, 1], [ng, -1]]) * (1/(2 * ng))

def D  (ng):
    return np.array([[1, 1], [ng, -ng]])