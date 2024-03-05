from Variables_for_Matrixes import*

LCM = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

LCM[0][0] = 1/8*((-I*rho_H**2*rho_E**4+(-I*rho_H**4-I+2*I*a2-4*I*rho_H**2)*rho_E**2+(-I+2*I*a2)*rho_H**2+4*I*a2)*DifS+2*rho_E**2*rho_H**2*DifC+(4*SumC-4*I*SumS)*a1-2*DifC)/a1
LCM[0][1] = -1/4*I*(-1/2*rho_E**2*rho_H**2-1/2+a2)*(rho_E+rho_H)*(-rho_H+rho_E)*DifS/a1
LCM[0][2] = 1/2*(rho_E+rho_H)*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E-a1*SumS+I*DifC+1/2*DifS)/Lo/rho_H/rho_E/no/omega/a1
LCM[0][3] = -1/2*(-rho_H+rho_E)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E+a1*SumS-1/2*DifS-I*DifC)*Pi/Lo/rho_H/rho_E/no/omega/a1
LCM[1][0] = 1/4*I*(-1/2*rho_E**2*rho_H**2-1/2+a2)*(rho_E+rho_H)*(-rho_H+rho_E)*DifS/a1
LCM[1][1] = 1/8*((I*rho_H**2*rho_E**4+(4*I*rho_H**2+I+I*rho_H**4-2*I*a2)*rho_E**2+(I-2*I*a2)*rho_H**2-4*I*a2)*DifS+2*rho_E**2*rho_H**2*DifC+(4*SumC+4*I*SumS)*a1-2*DifC)/a1
LCM[1][2] = 1/2*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-a1*SumS-I*DifC+1/2*DifS)*(-rho_H+rho_E)/Lo/rho_H/rho_E/no/omega/a1
LCM[1][3] = -1/2*(rho_E+rho_H)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-1/2*DifS+a1*SumS+I*DifC)*Pi/Lo/rho_H/rho_E/no/omega/a1
LCM[2][0] = -1/2*(rho_E+rho_H)*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E-a1*SumS+I*DifC+1/2*DifS)/Lo/no/omega/a1
LCM[2][1] = 1/2*(-rho_H+rho_E)*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-a1*SumS-I*DifC+1/2*DifS)*Pi/Lo/no/omega/a1
LCM[2][2] = 1/8*(-I*rho_H**2*rho_E**4*DifS-2*rho_E**3*rho_H**3*DifC+(-I*rho_H**4*DifS+((-4*I+4*I*a2)*DifS-4*I*SumS*a1)*rho_H**2+2*I*(-1/2+a2)*DifS)*rho_E**2+4*(1/2*DifC+SumC*a1)*rho_H*rho_E+2*I*(-1/2+a2)*rho_H**2*DifS)/rho_E/rho_H/a1
LCM[2][3] = 1/4*I*(rho_E+rho_H)*(-rho_H+rho_E)*DifS*(-1/2*rho_E**2*rho_H**2-1/2+a2)/rho_E/rho_H/a1
LCM[3][0] = -1/2*Pi*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E+a1*SumS-1/2*DifS-I*DifC)*(-rho_H+rho_E)/Lo/no/omega/a1
LCM[3][1] = 1/2*Pi*(rho_E+rho_H)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-1/2*DifS+a1*SumS+I*DifC)/Lo/no/omega/a1
LCM[3][2] = -1/4*I*(-rho_H+rho_E)*(rho_E+rho_H)*DifS*(-1/2*rho_E**2*rho_H**2-1/2+a2)/rho_E/rho_H/a1
LCM[3][3] = 1/8*(I*rho_H**2*rho_E**4*DifS-2*rho_E**3*rho_H**3*DifC+(I*rho_H**4*DifS+((4*I-4*I*a2)*DifS+4*I*SumS*a1)*rho_H**2-2*I*(-1/2+a2)*DifS)*rho_E**2+4*(1/2*DifC+SumC*a1)*rho_H*rho_E-2*I*(-1/2+a2)*rho_H**2*DifS)/rho_E/rho_H/a1



LDM = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

LDM[0][0] = 1 / 4 * ((2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o + epsilon_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (epsilon_o - 2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o)) / epsilon_o ** (1 / 2) / mu_o ** (1 / 2) / Nd
LDM[0][1] = 1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * (-epsilon_o + Nd ** 2 * mu_o)
LDM[0][2] = 0
LDM[0][3] = 0
LDM[1][0] = -1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * (-epsilon_o + Nd ** 2 * mu_o)
LDM[1][1] = -1 / 4 * ((epsilon_o - 2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o + epsilon_o)) / epsilon_o ** (1 / 2) / mu_o ** (1 / 2) / Nd
LDM[1][2] = 0
LDM[1][3] = 0
LDM[2][0] = 0
LDM[2][1] = 0
LDM[2][2] = 1 / 4 / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * ((rho_E ** 2 * epsilon_o + 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + Nd ** 2 * rho_H ** 2 * mu_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (Nd ** 2 * rho_H ** 2 * mu_o - 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + rho_E ** 2 * epsilon_o)) / Nd / rho_H / rho_E
LDM[2][3] = 1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / rho_H / mu_o ** (1 / 2) / rho_E / epsilon_o ** (1 / 2) * (-rho_E ** 2 * epsilon_o + Nd ** 2 * rho_H ** 2 * mu_o)
LDM[3][0] = 0
LDM[3][1] = 0
LDM[3][2] = -1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / rho_H / mu_o ** (1 / 2) / rho_E / epsilon_o ** (1 / 2) * (-rho_E ** 2 * epsilon_o + Nd ** 2 * rho_H ** 2 * mu_o)
LDM[3][3] = -1 / 4 / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * ((Nd ** 2 * rho_H ** 2 * mu_o - 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + rho_E ** 2 * epsilon_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (rho_E ** 2 * epsilon_o + 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + Nd ** 2 * rho_H ** 2 * mu_o)) / Nd / rho_H / rho_E

RBM = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

RBM[0][0] = 1 / 2 * (mu_o ** (1 / 2) * Nv + epsilon_o ** (1 / 2)) / Nv
RBM[0][1] = 1 / 2 * (mu_o ** (1 / 2) * Nv - epsilon_o ** (1 / 2)) / Nv
RBM[0][2] = 0
RBM[0][3] = 0
RBM[1][0] = 1 / 2 * (mu_o ** (1 / 2) * Nv - epsilon_o ** (1 / 2)) / Nv
RBM[1][1] = 1 / 2 * (mu_o ** (1 / 2) * Nv + epsilon_o ** (1 / 2)) / Nv
RBM[1][2] = 0
RBM[1][3] = 0
RBM[2][0] = 0
RBM[2][1] = 0
RBM[2][2] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv + rho_E * epsilon_o ** (1 / 2)) / Nv
RBM[2][3] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv - rho_E * epsilon_o ** (1 / 2)) / Nv
RBM[3][0] = 0
RBM[3][1] = 0
RBM[3][2] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv - rho_E * epsilon_o ** (1 / 2)) / Nv
RBM[3][3] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv + rho_E * epsilon_o ** (1 / 2)) / Nv

LBM = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

LBM[0][0] = 1/2*(mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
LBM[0][1] = 1/2*(-mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
LBM[0][2] = 0
LBM[0][3] = 0
LBM[1][0] = 1/2*(-mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
LBM[1][1] = 1/2*(mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
LBM[1][2] = 0
LBM[1][3] = 0
LBM[2][0] = 0
LBM[2][1] = 0
LBM[2][2] = 1/2*(rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
LBM[2][3] = 1/2*(-rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
LBM[3][0] = 0
LBM[3][1] = 0
LBM[3][2] = 1/2*(-rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
LBM[3][3] = 1/2*(rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)

TAJM =[[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

TAJM[0][0] = np.cos(D_D)
TAJM[0][1] = 0
TAJM[0][2] = -1 / 2 * (rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
TAJM[0][3] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
TAJM[1][0] = 0
TAJM[1][1] = np.cos(D_D)
TAJM[1][2] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
TAJM[1][3] = -1 / 2 * (rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
TAJM[2][0] = 1 / 2 * (rho_H + rho_E) * np.sin(D_D)
TAJM[2][1] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D)
TAJM[2][2] = np.cos(D_D)
TAJM[2][3] = 0
TAJM[3][0] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D)
TAJM[3][1] = 1 / 2 * (rho_H + rho_E) * np.sin(D_D)
TAJM[3][2] = 0
TAJM[3][3] = np.cos(D_D)