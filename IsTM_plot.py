import matplotlib.pyplot as plt

def plotTM(zg, Kg, Ag, Bg, Tg, ng):
    ABg = []
    #for i in range(len(Ag)):
    #    ABg.append(Ag[i] + Bg[i])
    if len(Kg) == 1:
        fig, ax = plt.subplots()
        ax.plot(zg, Ag, color =  'red', label = 'A')
        ax.plot(zg, Bg, color = 'blue', label = 'B')
        #ax.plot(zg, ABg, color = 'green', label = 'A + B')
        ax.scatter(zg, ng, s = 3, c = 'black')
        ax.set(xlabel = 'z', ylabel = 'Amplitude')
        ax.legend()
        plt.show()
    else:
        fig, ax = plt.subplots()
        ax.plot(Kg, Tg, color = 'red', label = 'Transmittance')
        ax.set(xlabel = 'Wave vector', title = 'Multilayer structure')
        ax.legend()
        plt.show()