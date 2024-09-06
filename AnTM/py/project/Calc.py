import numpy as np
import LiquidCrystal, Boundary, Vacuum, EMwave, LinearDefect, TwistDefect, LiquidCrystal2

#Constants for calculations
I = complex(0, 1)
Pi = np.pi

def create_omega_x(omega_min, omega_max):
  omega_x = np.linspace(omega_min, omega_max, 999)
  return omega_x

def create_TC(omega_x):
  TC = [0] * len(omega_x)
  
  return TC

def vo_calc(Theta, Phi):
  Theta_rad = Theta * (Pi / 180)
  Phi_rad = Phi * (Pi / 180)
  '''
  Vo = [
    np.cos(Theta_rad),
    0,
    np.sin(Theta_rad) * np.exp(I * Phi_rad),
    0
  ]
  '''
  Vo = [
    1/np.sqrt(2),
    0,
    I * (1/np.sqrt(2)),
    0
  ]
  return Vo

def tdm_calc(D_D):
  TDM = [
  [0, 0, 0, 0],
  [0, 0, 0, 0], 
  [0, 0, 0, 0],
  [0, 0, 0, 0]
  ]
  
  t1 = np.cos(D_D * (Pi / 180))
  t2 = np.sin(D_D * (Pi / 180))
  '''
  TDM[0][0] = t1 + I * t1
  TDM[1][1] = t1 + I * t1
  TDM[2][2] = t1 + I * t1
  TDM[3][3] = t1 + I * t1
  
  TDM[0][2] = -t2 - I * t2
  TDM[1][3] = -t2 - I * t2 
  TDM[2][0] = t2 + I * t2
  TDM[3][1] = t2 + I * t2
  '''
  TDM[0][0] = t1 
  TDM[1][1] = t1 
  TDM[2][2] = t1 
  TDM[3][3] = t1 
  
  TDM[0][2] = -t2 
  TDM[1][3] = -t2 
  TDM[2][0] = t2 
  TDM[3][1] = t2 
  return TDM

def lcm_calc(omega, No, Ne, Lo, L, X_M, xi): 
    
  A = (2 * np.sqrt(omega**2 * Lo**2 * No**4 + 16 * No**2 * Pi**2 - 2 * No**2 * Lo**2 * Ne**2 * omega**2 + 16 * Pi**2 * Ne * No * X_M + omega**2 * Lo**2 * Ne**4 + 16 * Ne**2 * Pi**2)) / (omega * np.abs(Lo))
  B = 2 * (Lo**2 * omega**2 * No**2 + Lo**2 * Ne**2 * omega**2 + 8 * Pi**2) / (Lo**2 * omega**2)

  Lp = L * omega / 2

  iotta = np.sqrt(A - B, dtype=np.complex128)
  sigma = np.sqrt(A + B)

  CI = np.cosh(Lp * iotta)
  CS = np.cos(Lp * sigma)
  SI = np.sinh(Lp * iotta) / iotta
  SS = np.sin(Lp * sigma) / sigma

  DifC = CI - CS
  DifS = SI - SS
  SumC = CI + CS
  SumS = SI + SS

  LCM = LiquidCrystal.Matrix
  '''
  LCM = [
    [0, 0, 0, 0],
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]
  '''
  LCM[0][0] = 1/2*((-2*I*X_M*No*Ne**2+(-8*I*No**2+2*I*B)*Ne+I*No*(-2*No**2+B)*X_M)*DifS+2*No**2*DifC-2*Ne**2*DifC+A*SumC-2*I*Ne*A*SumS)/A
  LCM[0][1] = -1/2*I*No*DifS*(-2*Ne**2-2*No**2+B)*(2+X_M)*(-2+X_M)/A/(2*xi-X_M)
  LCM[0][2] = -2*(2+X_M)*((No+Ne)**2*DifS-1/2*A*SumS+I*No*DifC+I*Ne*DifC)*Pi/Lo/omega/A/(xi+1)
  LCM[0][3] = -2*((Ne-No)**2*DifS-1/2*A*SumS-I*No*DifC+I*Ne*DifC)*(-2+X_M)*Pi/Lo/omega/A/(xi-1)
  LCM[1][0] = I*(-2*Ne**2-2*No**2+B)*(xi-1/2*X_M)*No*DifS/A
  LCM[1][1] = 1/2*((2*I*X_M*No*Ne**2+(8*I*No**2-2*I*B)*Ne-I*No*(-2*No**2+B)*X_M)*DifS+2*No**2*DifC-2*Ne**2*DifC+A*SumC+2*I*Ne*A*SumS)/A
  LCM[1][2] = 4*(-(Ne-No)**2*DifS-I*No*DifC+1/2*A*SumS+I*Ne*DifC)*(xi-1/2*X_M)*Pi/Lo/omega/A/(xi+1)
  LCM[1][3] = 4*(-(No+Ne)**2*DifS+I*Ne*DifC+1/2*A*SumS+I*No*DifC)*(xi-1/2*X_M)*Pi/Lo/omega/A/(xi-1)
  LCM[2][0] = 2*((No+Ne)**2*DifS-1/2*A*SumS+I*No*DifC+I*Ne*DifC)*Pi*(xi+1)/Lo/omega/A
  LCM[2][1] = 2*(-2+X_M)*(-(Ne-No)**2*DifS-I*No*DifC+1/2*A*SumS+I*Ne*DifC)*Pi*(xi+1)/Lo/omega/A/(2*xi-X_M)
  LCM[2][2] = 1/2*((-2*I*X_M*Ne**3-8*I*No*Ne**2+I*X_M*(-2*No**2+B)*Ne+2*I*No*B)*DifS-2*I*No*A*SumS+A*SumC-2*No**2*DifC+2*Ne**2*DifC)/A
  LCM[2][3] = 1/2*I*(xi+1)*Ne*DifS*(-2*Ne**2-2*No**2+B)*(-2+X_M)/A/(xi-1)
  LCM[3][0] = -2*Pi*(xi-1)*((Ne-No)**2*DifS-1/2*A*SumS-I*No*DifC+I*Ne*DifC)/Lo/omega/A
  LCM[3][1] = -2*Pi*(xi-1)*(2+X_M)*(-(No+Ne)**2*DifS+I*Ne*DifC+1/2*A*SumS+I*No*DifC)/A/Lo/omega/(2*xi-X_M)
  LCM[3][2] = -1/2*I*Ne*(-2*Ne**2-2*No**2+B)*DifS*(xi-1)*(2+X_M)/A/(xi+1)
  LCM[3][3] = 1/2*((2*I*X_M*Ne**3+8*I*No*Ne**2-I*(-2*No**2+B)*X_M*Ne-2*I*No*B)*DifS-2*No**2*DifC+2*Ne**2*DifC+A*SumC+2*I*No*A*SumS)/A
  
  return LCM

def lcm_calc2(omega, No, Ne, Lo, L, X_M, xi): 
    
  A = (2 * np.sqrt(omega**2 * Lo**2 * No**4 + 16 * No**2 * Pi**2 - 2 * No**2 * Lo**2 * Ne**2 * omega**2 + 16 * Pi**2 * Ne * No * X_M + omega**2 * Lo**2 * Ne**4 + 16 * Ne**2 * Pi**2)) / (omega * np.abs(Lo))
  B = 2 * (Lo**2 * omega**2 * No**2 + Lo**2 * Ne**2 * omega**2 + 8 * Pi**2) / (Lo**2 * omega**2)

  Lp = L * omega / 2

  iotta = np.sqrt(A - B, dtype=np.complex128)
  sigma = np.sqrt(A + B)

  CI = np.cosh(Lp * iotta)
  CS = np.cos(Lp * sigma)
  SI = np.sinh(Lp * iotta) / iotta
  SS = np.sin(Lp * sigma) / sigma

  DifC = CI - CS
  DifS = SI - SS
  SumC = CI + CS
  SumS = SI + SS

  LCM2 = LiquidCrystal2.Matrix
  '''
  LCM = [
    [0, 0, 0, 0],
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]
  '''
  LCM2[0][0] = 1/2*((-2*I*X_M*No*Ne**2+(-8*I*No**2+2*I*B)*Ne+I*No*(-2*No**2+B)*X_M)*DifS+2*No**2*DifC-2*Ne**2*DifC+A*SumC-2*I*Ne*A*SumS)/A
  LCM2[0][1] = -1/2*I*No*DifS*(-2*Ne**2-2*No**2+B)*(2+X_M)*(-2+X_M)/A/(2*xi-X_M)
  LCM2[0][2] = -2*(2+X_M)*((No+Ne)**2*DifS-1/2*A*SumS+I*No*DifC+I*Ne*DifC)*Pi/Lo/omega/A/(xi+1)
  LCM2[0][3] = -2*((Ne-No)**2*DifS-1/2*A*SumS-I*No*DifC+I*Ne*DifC)*(-2+X_M)*Pi/Lo/omega/A/(xi-1)
  LCM2[1][0] = I*(-2*Ne**2-2*No**2+B)*(xi-1/2*X_M)*No*DifS/A
  LCM2[1][1] = 1/2*((2*I*X_M*No*Ne**2+(8*I*No**2-2*I*B)*Ne-I*No*(-2*No**2+B)*X_M)*DifS+2*No**2*DifC-2*Ne**2*DifC+A*SumC+2*I*Ne*A*SumS)/A
  LCM2[1][2] = 4*(-(Ne-No)**2*DifS-I*No*DifC+1/2*A*SumS+I*Ne*DifC)*(xi-1/2*X_M)*Pi/Lo/omega/A/(xi+1)
  LCM2[1][3] = 4*(-(No+Ne)**2*DifS+I*Ne*DifC+1/2*A*SumS+I*No*DifC)*(xi-1/2*X_M)*Pi/Lo/omega/A/(xi-1)
  LCM2[2][0] = 2*((No+Ne)**2*DifS-1/2*A*SumS+I*No*DifC+I*Ne*DifC)*Pi*(xi+1)/Lo/omega/A
  LCM2[2][1] = 2*(-2+X_M)*(-(Ne-No)**2*DifS-I*No*DifC+1/2*A*SumS+I*Ne*DifC)*Pi*(xi+1)/Lo/omega/A/(2*xi-X_M)
  LCM2[2][2] = 1/2*((-2*I*X_M*Ne**3-8*I*No*Ne**2+I*X_M*(-2*No**2+B)*Ne+2*I*No*B)*DifS-2*I*No*A*SumS+A*SumC-2*No**2*DifC+2*Ne**2*DifC)/A
  LCM2[2][3] = 1/2*I*(xi+1)*Ne*DifS*(-2*Ne**2-2*No**2+B)*(-2+X_M)/A/(xi-1)
  LCM2[3][0] = -2*Pi*(xi-1)*((Ne-No)**2*DifS-1/2*A*SumS-I*No*DifC+I*Ne*DifC)/Lo/omega/A
  LCM2[3][1] = -2*Pi*(xi-1)*(2+X_M)*(-(No+Ne)**2*DifS+I*Ne*DifC+1/2*A*SumS+I*No*DifC)/A/Lo/omega/(2*xi-X_M)
  LCM2[3][2] = -1/2*I*Ne*(-2*Ne**2-2*No**2+B)*DifS*(xi-1)*(2+X_M)/A/(xi+1)
  LCM2[3][3] = 1/2*((2*I*X_M*Ne**3+8*I*No*Ne**2-I*(-2*No**2+B)*X_M*Ne-2*I*No*B)*DifS-2*No**2*DifC+2*Ne**2*DifC+A*SumC+2*I*No*A*SumS)/A
  
  return LCM2

def ldm_calc(omega, Nd, Ld):
  LDM = [
  [0, 0, 0, 0],
  [0, 0, 0, 0], 
  [0, 0, 0, 0],
  [0, 0, 0, 0]
  ]

  LDM[0][0] = np.exp(-I * Nd * omega * Ld)
  LDM[1][1] = np.exp(I * Nd * omega * Ld)
  LDM[2][2] = np.exp(-I * Nd * omega * Ld)
  LDM[3][3] = np.exp(I * Nd * omega * Ld)
  
  return LDM 

def bm_calc(epsilon_o_L, mu_o_L, epsilon_e_L, mu_e_L, epsilon_o_R, mu_o_R, epsilon_e_R, mu_e_R):
  BM = [
    [1, 0, 0, 0],
    [0, 1, 0, 0], 
    [0, 0, 1, 0],
    [0, 0, 0, 1]
    ]

  BM[0][0] = 0.5 + 0.5 * np.sqrt((mu_o_L * epsilon_o_R) / (mu_o_R * epsilon_o_L))
  BM[0][1] = 0.5 - 0.5 * np.sqrt((mu_o_L * epsilon_o_R) / (mu_o_R * epsilon_o_L))
  BM[0][2] = 0
  BM[0][3] = 0
  BM[1][0] = 0.5 - 0.5 * np.sqrt((mu_o_L * epsilon_o_R) / (mu_o_R * epsilon_o_L))
  BM[1][1] = 0.5 + 0.5 * np.sqrt((mu_o_L * epsilon_o_R) / (mu_o_R * epsilon_o_L))
  BM[1][2] = 0
  BM[1][3] = 0
  BM[2][0] = 0
  BM[2][1] = 0
  BM[2][2] = 0.5 + 0.5 * np.sqrt((mu_e_L * epsilon_e_R) / (mu_e_R * epsilon_e_L))
  BM[2][3] = 0.5 - 0.5 * np.sqrt((mu_e_L * epsilon_e_R) / (mu_e_R * epsilon_e_L))
  BM[3][0] = 0
  BM[3][1] = 0
  BM[3][2] = 0.5 - 0.5 * np.sqrt((mu_e_L * epsilon_e_R) / (mu_e_R * epsilon_e_L))
  BM[3][3] = 0.5 + 0.5 * np.sqrt((mu_e_L * epsilon_e_R) / (mu_e_R * epsilon_e_L))
  
  return BM

def fm_calc(List_of_finite_SM):
  FM = List_of_finite_SM[0]
  for i in range(1, len(List_of_finite_SM)):
      FM = np.dot(FM, List_of_finite_SM[i])
      
  return FM

def transmission_coef(FM, Vo):
  #Tx = (-Vo[2] * FM[0][2] + FM[2][2] * Vo[0]) / (FM[0][0] * FM[2][2] - FM[0][2] * FM[2][0])
  #Ty = -(Vo[0] * FM[2][0] - FM[0][0] * Vo[2]) / (FM[0][0] * FM[2][2] - FM[0][2] * FM[2][0])

  Tx = (FM[2][2] * Vo[0] - FM[0][2] * Vo[2]) / (- FM[2][0] * FM[0][2] + FM[2][2] * FM[0][0])
  Ty = - (-FM[0][0] * Vo[2] + FM[2][0] * Vo[0]) / (-FM[2][0] * FM[0][2] + FM[2][2] * FM[0][0])

  ###
  #print("Tx:", Tx)
  #print("Ty:", Ty)
  Tc = abs(Tx)** 2 + abs(Ty)** 2

  return Tc
