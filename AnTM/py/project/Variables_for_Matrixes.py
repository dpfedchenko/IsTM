import numpy as np
from Variables_on_interface import*
from Omega_dependent_calc import omega

I = complex(0, 1)
Pi = np.pi

epsilon_o = epsilon_o_value
mu_o = mu_o_value
rho_E = rho_E_value
rho_H = rho_H_value

Lo = Lo_value
L = L_value
Ld = Ld_value
Nd = Nd_value
Nv = Nv_value

D_D = D_D_value * np.pi / 180
Theta = Theta_value
Phi = Phi_value

#omega = omega_x[i]

no = np.sqrt(epsilon_o*mu_o)
ne = rho_E*rho_H*no

a2 = 1/2*(Lo**2*rho_H**2*rho_E**2*no**2*omega**2+8*Pi**2+Lo**2*no**2*omega**2)/Lo**2/no**2/omega**2
a1 = np.sqrt(1/4*(Lo**2*no**2*omega**2*rho_E**4*rho_H**4-2*Lo**2*rho_H**2*rho_E**2*no**2*omega**2+16*Pi**2*rho_E**2*rho_H**2+Lo**2*no**2*omega**2+16*Pi**2+16*Pi**2*rho_E**2+16*Pi**2*rho_H**2)/Lo**2/no**2/omega**2)

Lp = L * omega * no

iota = np.sqrt(a2 - a1, dtype=np.complex128)
sigma = np.sqrt(a1 + a2)

CI = np.cos(Lp*iota)
CS = np.cos(Lp*sigma)
SI = np.sin(Lp*iota)/iota
SS = np.sin(Lp*sigma)/sigma

DifC = CI-CS
DifS = SI-SS
SumC = CS+CI
SumS = SS+SI