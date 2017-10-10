#!/home/gabriel/anaconda3/bin/python3

import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

"""
Class that contains all functions
"""
class AnaliseRS:

    """
    This fuction gets the mean of the frequency for each size division.
    For example: When divided by 2, 183.
    When divided by 4, 91, and so on.
    """
    def FrequencyMean(self):
        freq_mean = []
        for x in range(0,6):
            freq_mean.append( int(len(self.btc)/math.pow(2, x)) )
        return freq_mean

    def analise(self):
        self.btc = open("btcHistory.txt", "r").read().split(" ")
        self.btc = list(map(float, self.btc))
        nroPontos = self.FrequencyMean()
        listaRS = [] #irá conter p rs de cada divisão
        mediaValor = 0
        for i in range(0,6): #This for runs through all possibel divisions of the values (divide in 1, in 2, in 4, in 8...)
            for j in range(0, int(math.pow(2,i)) ): #This one iterates over all n divisions
                rs = 0
                mediaValor = 0
                desvioAux = 0
                deviationSquare = 0
                desvios = []
                for k in range(0,nroPontos[i]): # Iterates over all values inside a division, and it calculates de sum of all btc values
                    l = k + j*nroPontos[i] #this 'l' is used because on each division I have to continue from where i finished the las one.
                    mediaValor += self.btc[l] #1. Calculate the mean

                mediaValor = mediaValor/nroPontos[i] #the mean inside each division
                for k in range(0,nroPontos[i]): # the same as the last for, but this time it calculates the standard deviation
                    l = k + j*nroPontos[i]
                    desvioAux += self.btc[l]-mediaValor # 3. Calculate the cumulative deviantions
                    deviationSquare += math.pow(self.btc[l]-mediaValor, 2) # Sum of squared deviantions, to calculate the standard deviantion
                    desvios.append(self.btc[l]-mediaValor) #I did a list of of all mean deviations so I can call "max" and "min" functions afte
                rt = max(desvios)-min(desvios)
                standardDeviation = math.sqrt(deviationSquare/nroPontos[i])
                rs += (rt/standardDeviation)
            rs = rs/math.pow(2,i)
            listaRS.append(math.log10(rs))

        pontosLog = []
        for x in nroPontos:
            pontosLog.append(math.log10(x))

        x = np.array(pontosLog).reshape(-1,1)

        model = LinearRegression()
        model.fit(x, listaRS)

        plt.scatter(x, listaRS, color='r')
        plt.plot(x, model.predict(x),color='k')
        slope, intercept = np.polyfit(pontosLog, listaRS, 1)
        plt.axis([-1.5, 3, -1.5, 3])
        plt.ylabel("Log R/S")
        plt.xlabel("Log size")
        plt.title(slope)
        plt.show()





if __name__ == "__main__":
    AnaliseRS().analise()
