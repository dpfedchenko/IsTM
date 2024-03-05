omega_x = [i for i in range(500 , 4001, 1)]
for i in range(0, len(omega_x)):
    omega_x[i] = omega_x[i]/500
U = [0]*len(omega_x)

for i in range(0, len(omega_x)):
    omega = omega_x[i]