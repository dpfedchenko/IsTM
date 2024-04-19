import Calc, LiquidCrystal, Boundary, Vacuum


def list_of_BM(Structure, StructureProperties):
    List_of_BM = []

    for i in range(0, len(Structure)-1):
      tmp_BM = Calc.bm_calc(
        StructureProperties[Structure[i]][0], 
        StructureProperties[Structure[i]][1],
        StructureProperties[Structure[i]][2], 
        StructureProperties[Structure[i]][3],
        StructureProperties[Structure[i+1]][0], 
        StructureProperties[Structure[i+1]][1],
        StructureProperties[Structure[i+1]][2], 
        StructureProperties[Structure[i+1]][3]
    )
      List_of_BM.append(tmp_BM)
    
    return List_of_BM

def list_of_finite_SM(LCM, LDM, TDM, LCM2, Structure, StructureProperties):
    List_of_StoM_transform = []
    List_of_finite_SM = []
    VM = [
        [1, 0, 0, 0],
        [0, 1, 0, 0], 
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    
    matrix_arr = [VM, LCM, LDM, TDM, LCM2]
    matrix_dict = {
        "V": 0,
        "LC": 1,
        "LD": 2,
        "TD": 3,
        "LC2": 4
    }

    for i in range(0, len(Structure)):
        idx = matrix_dict.get(Structure[i])
        List_of_StoM_transform.append(matrix_arr[idx])
    
    for i in range(0, len(list_of_BM(Structure, StructureProperties))):
        List_of_finite_SM += [List_of_StoM_transform[i], list_of_BM(Structure, StructureProperties)[i]]
    List_of_finite_SM += [VM]
    
    return List_of_finite_SM