import matplotlib.pyplot as plt
from calc import calculate_TO, calculate_OT, calculate_TE, Omega

TOa = calculate_TO()
OTa = calculate_OT()
UTEa = calculate_TE()

#plt.scatter(Omega, TOa, s = 15)
#plt.scatter(Omega, OTa, s = 2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in range(len(Omega) - 1):
    tx = UTEa[i][0]
    ty = UTEa[i][1]
    #ax.scatter(UTEa[i][0].real, Omega[i], UTEa[i][1].real, s = 2, c = 'r')
    #ax.scatter(UTEa[i][0].imag, Omega[i], UTEa[i][1].imag, s = 2, c = 'b')
    ax.scatter(tx.imag, Omega[i], ty.imag, s = 2, c = 'b')
plt.show()