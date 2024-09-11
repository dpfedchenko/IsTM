import numpy as np
import matplotlib.pyplot as plt
import Calc2, LiquidCrystal, Boundary, Vacuum, StructureBuilding, EMwave, LinearDefect, TwistDefect, plot, LiquidCrystal2

# Create structure
Structure = ["V", "LC" , "LC", "LD","LC", "V"]  

StructureProperties = {
  "V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
  "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e],
  "LD": [LinearDefect.epsilon_o, LinearDefect.mu_o, LinearDefect.epsilon_e, LinearDefect.mu_e],
  "TD": [TwistDefect.epsilon_o, TwistDefect.mu_o, TwistDefect.epsilon_e, TwistDefect.mu_e],
  "LC2": [LiquidCrystal2.epsilon_o, LiquidCrystal2.mu_o, LiquidCrystal2.epsilon_e, LiquidCrystal2.mu_e]}

StructureMatrixes = {
  "V": Vacuum.unit_VM,
  "LC": Calc2.lcm_calc,
  "LD": Calc2.ldm_calc,
  "TD": Calc2.tdm_calc,
  "LC2": Calc2.lcm_calc2}

omega_x = Calc2.create_omega_x(5, 15)
TC = Calc2.create_TC(omega_x)

for i in range(0, len(omega_x)):
    omega = omega_x[i]
    List_of_finite_SM = StructureBuilding.list_of_finite_SM(
      Calc2.lcm_calc(omega, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi),
      Calc2.ldm_calc(omega, LinearDefect.No, LinearDefect.L),
      Calc2.tdm_calc(TwistDefect.D_D),
      Calc2.lcm_calc2(omega, LiquidCrystal2.No, LiquidCrystal2.Ne, LiquidCrystal2.Lo, LiquidCrystal2.L, LiquidCrystal2.X_M, LiquidCrystal2.xi), 
      Structure, 
      StructureProperties
      )
    FM = Calc2.fm_calc(List_of_finite_SM)
    Vo = Calc2.vo_calc(EMwave.Theta, EMwave.Phi)
    Tc = Calc2.transmission_coef(FM, Vo)
    TC[i] = Tc

# Plot
plot.plot_TD(omega_x, TC, 600, 750, 'red')





