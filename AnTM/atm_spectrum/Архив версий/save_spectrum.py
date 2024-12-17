from assign import KR

ledge = str(int(KR[1]**(-1) * 1000))
redge = str(int(KR[0]**(-1) * 1000))

with open('atm_spectrum/wavelength_' + ledge + '_' + redge + '.txt', 'w') as atmf:
    for item in spectrum_atm[0]: 
        atmf.write(str(item) + '\n')

with open('atm_spectrum/transmittance_' + ledge + '_' + redge + '.txt', 'w') as atmf:
    for item in spectrum_atm[1]: 
        atmf.write(str(item) + '\n')