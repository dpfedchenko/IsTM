import numpy as np
import matplotlib.pyplot as plt
import Calc, LiquidCrystal, Boundary, Vacuum, StructureBuilding, EMwave, LinearDefect, TwistDefect, plot, LiquidCrystal2, SetStructure

#Structure = ["V", "LC", "TD", "LC2", "TD","LC", "V"]  
Structure = SetStructure.Structure
#Structure = ["V", "LC", "V"]

StructureProperties = SetStructure.StructureProperties

StructureMatrixes = {
  "V": Vacuum.unit_VM,
  "LC": Calc.lcm_calc,
  "LD": Calc.ldm_calc,
  "TD": Calc.tdm_calc,
  "LC2": Calc.lcm_calc2
  }

#ax = plt.figure().add_subplot(projection='3d')
omega_x = Calc.create_omega_x(2, 5)
TC = Calc.create_TC(omega_x)

'''
#Lo_values = np.linspace(1, 51, 10)

List_of_BM = StructureBuilding.list_of_BM(Structure, StructureProperties)
for j in Lo_values:
  for i in range(0, len(omega_x)):
    omega = omega_x[i]
    List_of_finite_SM = StructureBuilding.list_of_finite_SM(
      Calc.lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi),
      Calc.ldm_calc(omega, LinearDefect.No, LinearDefect.L),
      Calc.tdm_calc(TwistDefect.D_D),
      Calc.lcm_calc2(omega, LiquidCrystal2.No, LiquidCrystal2.Ne, j, LiquidCrystal2.L, LiquidCrystal2.X_M, LiquidCrystal2.xi), 
      Structure, 
      StructureProperties
      )
    FM = Calc.fm_calc(List_of_finite_SM)
    Vo = Calc.vo_calc(EMwave.Theta, EMwave.Phi)
    Tc = Calc.transmission_coef(FM, Vo)
    TC[i] = Tc
  
  ax.plot(omega_x, [j] * len(omega_x), TC)  
'''    

for i in range(0, len(omega_x)):
    omega = omega_x[i]
    List_of_finite_SM = StructureBuilding.list_of_finite_SM(
      Calc.lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi),
      Calc.ldm_calc(omega, LinearDefect.No, LinearDefect.L),
      Calc.tdm_calc(TwistDefect.D_D),
      Calc.lcm_calc2(omega, LiquidCrystal2.No, LiquidCrystal2.Ne, LiquidCrystal2.Lo, LiquidCrystal2.L, LiquidCrystal2.X_M, LiquidCrystal2.xi), 
      Structure, 
      StructureProperties
      )
    FM = Calc.fm_calc(List_of_finite_SM)
    Vo = Calc.vo_calc(EMwave.Theta, EMwave.Phi)
    Tc = Calc.transmission_coef(FM, Vo)
    TC[i] = Tc

##with open('lc_ld_lc108.txt', 'w') as file:
##  file.write('omega:    Tc: \n')
##
##  for i in range(len(omega_x)):
##    file.write(f"{omega_x[i]}    {TC[i]}\n")

##plot.plot_transmission_spectra_OxWaveLength(omega_x, TC)    
##plot.plot_transmission_spectra(omega_x, TC)
#plot.plot_TD(omega_x, TC, 600, 750, 'red')


'''
plot.plot_TC_dTC(omega_x, TC, Calc.derivative(omega_x, TC))
Calc.Q_value_via_TcFunc()
Calc.Q_value(omega_x, TC, Calc.derivative(omega_x, TC))
'''

plot.plot_TC_dTC(omega_x, TC, Calc.derivative(omega_x, TC))

print(f'Calculate the value of the Q-factor? \n"yes" or "no"')
answer_Qfactor = str(input())
if answer_Qfactor == 'yes':
  Calc.Q_value_via_TcFunc()
'''
#Calc.Q_value(omega_x, TC, Calc.derivative(omega_x, TC))
#plot.plot_transmission_spectra_OxWaveLength(omega_x, TC)    
#plot.plot_transmission_spectra(omega_x, TC)
#plot.plot_diff_Tw(omega_x, TC)



>>>>>>> e771c5a2896e21c8de98635712e883388dd82592
'''









