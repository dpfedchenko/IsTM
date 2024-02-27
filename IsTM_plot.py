import matplotlib.pyplot as plt

# TMS
def plotTM(zg, Kg, rAg, rBg, Tg, _rAg, _rBg, _Tg):
    diffTg = []
    for i in range(len(Tg)):
        diffTg.append(Tg[i] - _Tg[i])
    if len(Kg) == 1:
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(zg, _rAg, color = 'red', label = 'A.real')
        ax[0].plot(zg, _rBg, color = 'blue', label = 'B.real')
        ax[0].set(xlabel='z', ylabel=' ', title='The opposite direction')
        ax[0].set(xlabel='z', ylabel=' ')
        ax[0].legend()
        
        ax[1].plot(zg, rAg, color = 'red', label = 'A.real')
        ax[1].plot(zg, rBg, color = 'blue', label = 'B.real')
        ax[1].set(xlabel='z', ylabel=' ', title='The right direction')
        ax[1].set(xlabel='z', ylabel=' ')
        ax[1].legend()

        plt.show()
    else:
        fig, ax = plt.subplots(1, 2)
        ax[0].plot(Kg, _Tg, color = 'red', label = '$T^\prime$')
        ax[0].plot(Kg, diffTg, color = 'blue', label = '$T - T^\prime$')
        ax[0].set(xlabel='Wave vector', ylabel='Transmittance',  title='The opposite direction')
        ax[0].legend()
        

        ax[1].plot(Kg, Tg, color = 'red', label = '$T$')
        ax[1].set(xlabel='Wave vector', title='The right direction')
        ax[1].legend()

        plt.show()