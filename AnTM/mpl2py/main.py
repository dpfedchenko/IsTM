import matplotlib.pyplot as plt
from calc import calculate_TO, calculate_OT
from calc_sym import calculate_TO_sym, calculate_OT_sym
from assign import Pi, KR, lmbd
from Berreman import tBSp, BSp
import numpy as np

TOspec = calculate_TO_sym()
OTspec = calculate_OT_sym()

plt.plot(lmbd, TOspec, linewidth = 6, label = 'ATM TO')
plt.plot(lmbd, OTspec, label = 'ATM OT')

plt.plot(tBSp, BSp, c = 'm', label = 'Berreman')

plt.legend()
plt.show()