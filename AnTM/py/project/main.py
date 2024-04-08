import numpy as np
import Calc, LiquidCrystal, Boundary, Vacuum, StructureBuilding

omega_x = np.linspace(1, 8, 1000)
TC = [0] * len(omega_x)

Structure = ["V", "LC", "V"]
StructureProperties = {"V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
                       "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e]}
StructureMatrixes = {"V": Vacuum.unit_VM,
                     "LC": Calc.lcm_calc}


List_of_BM = StructureBuilding.list_of_BM(Structure, StructureProperties)
List_of_finite_SM = StructureBuilding.list_of_finite_SM(Calc.lcm_calc(6.0, LiquidCrystal.No, LiquidCrystal.Ne, LiquidCrystal.Lo, LiquidCrystal.L, LiquidCrystal.X_M, LiquidCrystal.xi), Structure, StructureProperties)
print("List_of_BM")
print(*List_of_BM[0], sep="\n")
print(*List_of_BM[1], sep="\n")

print("len:", len(List_of_finite_SM))
print("List_of_finite_SM")
print(*List_of_finite_SM[0], sep="\n")
print(*List_of_finite_SM[1], sep="\n")
print(*List_of_finite_SM[2], sep="\n")
print(*List_of_finite_SM[3], sep="\n")
print(*List_of_finite_SM[4], sep="\n")

FM = Calc.fm_calc(List_of_finite_SM)
print("FM")
print(FM)











