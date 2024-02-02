import numpy as np

def TMM (n1, n2, AB, Str):
    N = len(Str)
    A = []
    B = []
    
    ABz = AB
    A.append(abs(ABz[0]))
    B.append(abs(ABz[1]))
    
    for i in range(N):
        z = i / (2*N)
        n_cl = (Str[i] % 2) * n2 + (1 - Str[i]%2) * n1
        n_pr = (Str[i] % 2) * n1 + (1 - Str[i]%2) * n2
        
        Dcl = np.array([[1, 1],
                     [n_cl, -n_cl]])
        iDpr = np.array([[n_pr, 1],
                        [n_pr,-1]]) 
        
        T = (0.5 * n_pr) * iDpr @ Dcl 
        
        ABz = T @ ABz
        
        A.append(abs(ABz[0]))
        B.append(abs(ABz[1]))
    return [A, B]
        
    
def fIsTM(n1, n2, lmbd, L, AB, Str):
    I = complex(0, 1)
    C = n1/n2
    w = 2*np.pi/lmbd

    A = []
    B = []
    
    ABz = AB
    A.append(abs(ABz[0]))
    B.append(abs(ABz[1]))

    P = len(Str)
    
    for i in range(P):
        z = -(i * L)/P
        
        # Подумать как задавать структуру (как в TB!)
        k = (Str[i] % 2) * n2 * w + (1 - Str[i]%2) * n1 * w
        С = (Str[i] % 2) * (n2/n1) + (1 - Str[i]%2) * (n1/n2)
        
        # Карго!
        M = np.array([[(1 + C)*np.exp(-I*k*z), (1 - C)*np.exp(I*k*z)],
                [(1 - C)*np.exp(-I*k*z), (1 + C)*np.exp(I*k*z)]])
        
        ABz = (0.5 * M) @ ABz

        A.append(abs(ABz[0]))
        B.append(abs(ABz[1]))

        print(ABz)

    return [A, B]
