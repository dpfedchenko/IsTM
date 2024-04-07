import Calc, LiquidCrystal, Boundary, Vacuum

Structure = ["V", "LC", "V"]
StructureProperties = {"V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
                       "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e]}
StructureMatrixes = {"V": Vacuum.Matrix,
                     "LC": Calc.lcm_calc}


def list_of_BM():
    List_of_BM = []

    for i in range(0, len(Structure)-1):
        tmp_BM = Calc.bm_calc(StructureProperties[Structure[i]][0], 
                              StructureProperties[Structure[i]][1],
                              StructureProperties[Structure[i]][2], 
                              StructureProperties[Structure[i]][3],
                              StructureProperties[Structure[i+1]][0], 
                              StructureProperties[Structure[i+1]][1],
                              StructureProperties[Structure[i+1]][2], 
                              StructureProperties[Structure[i+1]][3])
        List_of_BM.append(tmp_BM)
    
    return List_of_BM

def list_of_finite_SM(VM, LCM):
    List_of_StoM_transform = []
    List_of_finite_SM = []
    
    matrix_arr = [VM, LCM]
    matrix_dict = {"V": 0,
                   "LC": 1}

    for i in range(0, len(Structure)):
        idx = matrix_dict.get(Structure[i])
        List_of_StoM_transform.append(matrix_arr[i])
    
    for i in range(0, len(list_of_BM)):
        List_of_finite_SM += [List_of_StoM_transform[i], list_of_BM[i]]

        if i == len(list_of_BM):
            List_of_finite_SM += [VM]
    
    return List_of_finite_SM





