from calc import T_spectrum_calc_to, T_spectrum_calc_ot 
from plot import T_spectrum_plot

Uto = T_spectrum_calc_to()
Uot = T_spectrum_calc_ot()

T_spectrum_plot(Uto, Uot)
