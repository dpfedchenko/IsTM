import matplotlib.pyplot as plt
def plotTM(zg, Kg, Ag, Bg, Tg, ng):
    ABg = []
    for i in range(len(Ag)): ABg.append(abs(Ag[i] + Bg[i]))
    if len(Kg) == 1:
        fig, ax = plt.subplots()
        ax.plot(zg, Ag, color =  'red', label = 'A')
        ax.plot(zg, Bg, color = 'blue', label = 'B')
        ax.plot(zg, ABg, color = 'magenta', label = '|A + B|')
        for i in range (len(zg) - 1): ax.plot([zg[i], zg[i + 1]], [ng[i], ng[i + 1]], c = '#00ff00')
        ax.set(xlabel = 'z', ylabel = 'Value')
        ax.legend()
        plt.show()
    else:
        fig, ax = plt.subplots()
        ax.plot(Kg, Tg, color = 'red')
        ax.set(xlabel = 'Wave vector', ylabel = 'Transmittance')
        plt.show()