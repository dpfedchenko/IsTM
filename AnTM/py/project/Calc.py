import numpy as np
from scipy.interpolate import CubicSpline, interp1d
import LiquidCrystal, Boundary, Vacuum, EMwave, LinearDefect, TwistDefect, LiquidCrystal2
import StructureBuilding, SetStructure
import matplotlib.pyplot as plt
import time

#Constants for calculations
I = complex(0, 1)
Pi = np.pi

def create_omega_x(omega_min, omega_max):

  omega_x = np.linspace(omega_min, omega_max, 50000)
  
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

def derivative(x, y):
  
  dy = np.diff(y)
  dx = np.diff(x)
  dy_dx = dy / dx
  
  x_derivative = x[:-1]
  normalize_dy_dx = (dy_dx / (max(dy_dx) - min(dy_dx))) + abs(min((dy_dx / (max(dy_dx) - min(dy_dx)))))
  
  dy0 = abs(min((dy_dx / (max(dy_dx) - min(dy_dx)))))
  
  return x_derivative, normalize_dy_dx, dy0
  
def Q_value(x, y, derivative):
  
  # ВЫДЕЛЕНИЕ ОБЛАСТИ С ПИКОМ
  dx, dy_dx, dy_dx0 = derivative
  
  idx_of_max_dy_dx = np.argmax(dy_dx)
  idx_of_min_dy_dx = np.argmin(dy_dx)
  
  #print(f'index of max dy/dx = {idx_of_max_dy_dx}')
  #print(f'index of min dy/dx = {idx_of_min_dy_dx}')
  
  
  #print(f'Поиск правого нуля проивзодной: \n')
  for i in range(idx_of_min_dy_dx, len(dx), 1):
    if (dy_dx[i] > dy_dx0):
      idx_right_null = i
      value_right_null = dy_dx[i]
      omega_border_right = dx[i]
      break
    else: 
      i+=1
  
  #print(f'index of right 0 = {idx_right_null}')   
  #print(f'value of right 0 = {value_right_null}')  
  #print(f'value of omega right border = {omega_border_right}') 
  
  #print(f'Поиск левого нуля производной')
  
  for i in range(idx_of_max_dy_dx, 0, -1):
    if(dy_dx[i] < dy_dx0):
      idx_left_null = i
      value_left_null = dy_dx[i]
      omega_border_left = dx[i]
      break
    else:  
      i-=1
  
  #print(f'index of left 0 = {idx_left_null}')   
  #print(f'value of left 0 = {value_left_null}')
  #print(f'value of omega left border = {omega_border_left}')   
  
  cropped_y = y[idx_left_null:idx_right_null]
  cropped_x = x[idx_left_null:idx_right_null]
  
  max_cropped_y = max(cropped_y)
  idx_max_cropped_y = np.argmax(cropped_y)
  omega_of_max_transmission = cropped_x[idx_max_cropped_y]
  
  #print(f'max value of transmission = {max_cropped_y} = {max_cropped_y*100}% ')
  #print(f'index of max value of transmission = {idx_max_cropped_y}')
  #rint(f'omega of max transmisison = {omega_of_max_transmission}')
  
  
  ## Сплайн-интерполяция + линейная интерполяция для полуширины
  ########################################################################################################################################################
  CubSpl = CubicSpline(cropped_x, cropped_y)
  SplineItp_cropped_x = np.linspace(cropped_x[0], cropped_x[-1], 100000)
  SplineItp_cropped_y = CubSpl(SplineItp_cropped_x)
  
  ### Определение максимального значения пропускания и соответствующей ему частоты
  max_SplineItp_cropped_y = max(SplineItp_cropped_y)
  idx_max_SplineItp_cropped_y = np.argmax(SplineItp_cropped_y)
  omega_of_maxTransmission_SplineItp = SplineItp_cropped_x[idx_max_SplineItp_cropped_y]
  
  print(f'\nMax value of transmission (SplItp) = {max_SplineItp_cropped_y} = {max_SplineItp_cropped_y*100:.2f}%')
  print(f'Omega of max value of transmission (SplItp) = {omega_of_maxTransmission_SplineItp}')
  print()
  
  ### Определение частот при которых пропускание равно половине от максимального (полувысоте)
  half_height_SplineItp = max_SplineItp_cropped_y / 2
  
  Q_left_w_area = SplineItp_cropped_x[0:idx_max_SplineItp_cropped_y]
  Q_left_T_area = SplineItp_cropped_y[0:idx_max_SplineItp_cropped_y]
  
  Q_right_w_area = SplineItp_cropped_x[idx_max_SplineItp_cropped_y:-1]
  Q_right_T_area = SplineItp_cropped_y[idx_max_SplineItp_cropped_y:-1]
  
  interp_func_left = interp1d(
    Q_left_T_area, 
    Q_left_w_area, 
    kind='linear', 
    bounds_error=False, 
    fill_value='extrapolate'
  )
  
  interp_func_right = interp1d(
    Q_right_T_area,
    Q_right_w_area,
    kind='linear', 
    bounds_error=False, 
    fill_value='extrapolate'
  )
  
  left_w_at_hal_height = interp_func_left(half_height_SplineItp)
  right_w_at_hal_height = interp_func_right(half_height_SplineItp)
  hw_at_hh = right_w_at_hal_height - left_w_at_hal_height
  
  print(f'W1(T = T_max/2) = {left_w_at_hal_height}')
  print(f'W2(T = T_max/2) = {right_w_at_hal_height}')
  print(f'deltaW at hh = {hw_at_hh}')
  print()
  
  Q = omega_of_maxTransmission_SplineItp / hw_at_hh
  
  #print(f'Добротность \nQ = {Q}')
  
  exponent = int(np.floor(np.log10(Q)))
  mantissa = Q / (10 ** exponent)
  formated_Q = f'{mantissa:.3f}e{exponent}'
  
  print(f'Добротность \nQ = {Q} = {formated_Q}')

  ######################################################################################################################################################## 
  
  plt.plot(SplineItp_cropped_x, SplineItp_cropped_y, label='spline interpolation') 
  plt.plot(cropped_x, cropped_y, 'o',color='red')
  plt.yticks(np.arange(0, 1.25, 0.25))
  plt.grid()
  plt.show()

def Q_value_via_TcFunc():
  
  print()
  print(f'Choose frequency area to calculate Q value')
  
  print(f'Set init omega:')
  w1 = float(input())
  print(f'Set finite omega:')
  w2 = float(input())
  
  print(f'\n!!! Choose accuracy of calculation !!!')
  print('Set steps between w1 and w2:')
  steps = int(input())
  print()
  
  start_time = time.time()
  
  frequencies_range = np.linspace(w1, w2 + (w2-w1) / steps, steps)
  TC = create_TC(frequencies_range)
  
  for i in range(0, len(frequencies_range)):
    omega = frequencies_range[i]
    List_of_finite_SM = StructureBuilding.list_of_finite_SM(
      lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi),
      ldm_calc(omega, LinearDefect.No, LinearDefect.L),
      tdm_calc(TwistDefect.D_D),
      lcm_calc2(omega, LiquidCrystal2.No, LiquidCrystal2.Ne, LiquidCrystal2.Lo, LiquidCrystal2.L, LiquidCrystal2.X_M, LiquidCrystal2.xi), 
      SetStructure.Structure, 
      SetStructure.StructureProperties
      )
    FM = fm_calc(List_of_finite_SM)
    Vo = vo_calc(EMwave.Theta, EMwave.Phi)
    Tc = transmission_coef(FM, Vo)
    TC[i] = Tc
  
  maximum_transmission = max(TC)
  idx_of_maxTransmission = np.argmax(TC)
  frequency_of_maxTransmission = frequencies_range[idx_of_maxTransmission]
  
  print()
  print(f'Maximum tramsmission = {maximum_transmission} = {100 * maximum_transmission:.4f}%')
  print(f'Frequency of max transmission = {frequency_of_maxTransmission}')
  print()
  
  half_height = maximum_transmission / 2
  
  left_range_of_frequensies = frequencies_range[0:idx_of_maxTransmission]
  left_range_of_Transmission = TC[0:idx_of_maxTransmission]
  
  right_range_of_frequensies = frequencies_range[idx_of_maxTransmission:-1]
  right_range_of_Transmission = TC[idx_of_maxTransmission:-1]
  
  interp_func_left = interp1d(
    left_range_of_Transmission,
    left_range_of_frequensies,
    kind='linear', 
    bounds_error=False, 
    fill_value='extrapolate'
  )
  
  interp_func_right = interp1d(
    right_range_of_Transmission,
    right_range_of_frequensies,
    kind='linear', 
    bounds_error=False, 
    fill_value='extrapolate'
  )
  
  left_w_at_hal_height = interp_func_left(half_height)
  right_w_at_hal_height = interp_func_right(half_height)
  hw_at_hh = right_w_at_hal_height - left_w_at_hal_height
  
  print()
  print(f'W1 at T_max/2 = {left_w_at_hal_height}')
  print(f'W2 at T_max/2 = {right_w_at_hal_height}')
  print(f'deltaW at hh = {hw_at_hh}')
  print()
  
  
  Q = frequency_of_maxTransmission / hw_at_hh
  
  exponent = int(np.floor(np.log10(Q)))
  mantissa = Q / (10 ** exponent)
  formated_Q = f'{mantissa:.3f}e{exponent}'
  
  print()
  print(f'Length of LC shoulder = {LiquidCrystal.L}')
  print(f'Q-factor \nQ = {Q} = {formated_Q}')
  print()
  
  end_time = time.time()
  calc_time = end_time - start_time
  print()
  print(f'Calculation time of Q-factor: {calc_time:.3f} second')
  print()
  
  plt.scatter(frequencies_range, TC)
  plt.yticks(np.arange(0, 1.25, 0.25))
  plt.grid()
  plt.show()
  
  
  
  
  
  
  
  
  
    
  
  
    
        
      
  
  

  
  
  
   
  

  
  
  
  
  

