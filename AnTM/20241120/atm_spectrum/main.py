from calc import TA_spectrum_calc 
from plot import T_spectrum_plot
from assign import KR

spectral_coefficients = TA_spectrum_calc()
spectrum_atm = T_spectrum_plot(spectral_coefficients[0], spectral_coefficients[1], spectral_coefficients[2])

"""
ledge = str(int(KR[1]**(-1) * 1000))
redge = str(int(KR[0]**(-1) * 1000))

with open('atm_spectrum/wavelength_' + ledge + '_' + redge + '.txt', 'w') as atmf:
    for item in spectrum_atm[0]: 
        atmf.write(str(item) + '\n')

with open('atm_spectrum/transmittance_' + ledge + '_' + redge + '.txt', 'w') as atmf:
    for item in spectrum_atm[1]: 
        atmf.write(str(item) + '\n')
"""