def printE (E):
    for i in range(len(E)):
        print(str("{:.2f}".format(E[i][0])) + ", " + str("{:.2f}".format(E[i][1])))
def print2M (M):
    print(str("{:.2f}".format(M[0][0])) + " | " + str("{:.2f}".format(M[0][1])))
    print(str("{:.2f}".format(M[1][0])) + " | " + str("{:.2f}".format(M[1][1])))
