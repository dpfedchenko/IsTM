from assign import lmbd
from calc import calculate_TO, calculate_OT
from Berreman import tBSp, BSp
from Maple_ATM import tMSp, MSp
import matplotlib.pyplot as plt

TO_spectrum = calculate_TO()
OT_spectrum = calculate_OT()

plt.plot(lmbd[::-1], TO_spectrum[::-1], linewidth = 5, label = 'ATM TO')
plt.plot(lmbd[::-1], OT_spectrum[::-1], label = 'ATM OT')

#plt.plot(tBSp, BSp, c = 'm', label = 'Berreman')
#plt.plot(tMSp, MSp, c = 'y', label = 'Maple ATM')

plt.legend()
plt.show()