from calc import TA_spectrum_calc 
from plot import T_spectrum_plot

spectral_coefficients = TA_spectrum_calc()
spectrum_atm = T_spectrum_plot(spectral_coefficients)