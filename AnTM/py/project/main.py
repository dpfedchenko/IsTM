import numpy as np
import Calc, LiquidCrystal, Boundary, Vacuum, StructureBuilding, EMwave, LinearDefect, TwistDefect, plot

Structure = ["V","LC", "LD", "LC", "V"]
StructureProperties = {
  "V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
  "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e],
  "LD": [LinearDefect.epsilon_o, LinearDefect.mu_o, LinearDefect.epsilon_e, LinearDefect.mu_e],
  "TD": [TwistDefect.epsilon_o, TwistDefect.mu_o, TwistDefect.epsilon_e, TwistDefect.mu_e]
  }

StructureMatrixes = {
  "V": Vacuum.unit_VM,
  "LC": Calc.lcm_calc,
  "LD": Calc.ldm_calc,
  "TD": Calc.tdm_calc
  }

omega_x = Calc.create_omega_x(1, 10)
TC = Calc.create_TC(omega_x)

List_of_BM = StructureBuilding.list_of_BM(Structure, StructureProperties)

for i in range(0, len(omega_x)):
  omega = omega_x[i]
  List_of_finite_SM = StructureBuilding.list_of_finite_SM(
    Calc.lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi),
    Calc.ldm_calc(omega, LinearDefect.No, LinearDefect.L),
    Calc.tdm_calc(TwistDefect.D_D), 
    Structure, 
    StructureProperties
    )
  FM = Calc.fm_calc(List_of_finite_SM)
  Vo = Calc.vo_calc(EMwave.Theta, EMwave.Phi)
  Tc = Calc.transmission_coef(FM, Vo)
  TC[i] = Tc

plot.plot_transmission_spectra(omega_x, TC)











