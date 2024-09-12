import matplotlib.pyplot as plt
def plotTM(zg, Kg, Ag, Bg, Tg, ng):
    ABg = []
    if len(Kg) == 1:
        fig, ax = plt.subplots()
        ax.plot(zg, Ag, color =  'red', label = 'A')
        ax.plot(zg, Bg, color = 'blue', label = 'B')
        ax.scatter(zg, ng, s = 3, c = '#00ff00')
        ax.set(xlabel = 'z', ylabel = 'Value')
        ax.legend()
        plt.show()
    else:
        fig, ax = plt.subplots()
        ax.plot(Kg, Tg, color = 'red')
        ax.set(xlabel = 'Wave vector', ylabel = 'Transmittance')
        plt.show()