import numpy as np
import Calc, LiquidCrystal, Boundary, Vacuum, StructureBuilding

omega_x = np.linspace(1, 8, 1000)
TC = [0] * len(omega_x)

Structure = ["V", "LC", "V"]
StructureProperties = {"V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
                       "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e]}
StructureMatrixes = {"V": Vacuum.Matrix,
                     "LC": Calc.lcm_calc}


test1 = StructureBuilding.list_of_BM(Structure, StructureProperties)
print(test1)

