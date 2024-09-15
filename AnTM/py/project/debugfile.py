import numpy as np
import Calc, LiquidCrystal, Boundary, Vacuum, StructureBuilding, EMwave, LinearDefect, plot

Structure = ["V", "LD", "V"]
StructureProperties = {
  "V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
  "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e],
  "LD": [LinearDefect.epsilon_o, LinearDefect.mu_o, LinearDefect.epsilon_e, LinearDefect.mu_e]
  }

StructureMatrixes = {
  "V": Vacuum.unit_VM,
  "LC": Calc.lcm_calc,
  "LD": Calc.ldm_calc
  }

omega_x = Calc.create_omega_x(1, 8)
TC = Calc.create_TC(omega_x)

List_of_BM = StructureBuilding.list_of_BM(Structure, StructureProperties)


omega = 4.0
List_of_finite_SM = StructureBuilding.list_of_finite_SM(
  Calc.lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi), 
  Calc.ldm_calc(omega, LinearDefect.No, LinearDefect.L),
  Structure, 
  StructureProperties
  )

print("List_of_BM")
for i in range(0, len(List_of_BM)):
  print(*List_of_BM[i], sep="\n")

print("len:", len(List_of_finite_SM))
print("List_of_finite_SM")
for i in range(0, len(List_of_finite_SM)):
  print(*List_of_finite_SM[i], sep="\n")


FM = Calc.fm_calc(List_of_finite_SM)
print("FM")
#print(*FM)
for i in range(0, 4):
  for j in range(0, 4):
    print("FM[",i,"][",j,"] = ", FM[i][j])
    

Vo = Calc.vo_calc(EMwave.Theta, EMwave.Phi)
print("Vo")
print(Vo)


Tc = Calc.transmission_coef(FM, Vo)
print("Tc")
print(Tc)
#plot.plot_transmission_spectra(omega_x, TC)













