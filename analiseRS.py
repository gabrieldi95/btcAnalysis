#!/home/gabriel/anaconda3/bin/python3

import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


class AnaliseRS:

    
    def media_de_pontos(self):
        """
            Returns a list of the number of values in each division. So if your data
            has 300 values, the first number on the list will be 300, than 150, then
            75, and so on, wich is the mean of the frequency of values in each division.
        """
        media_pontos = []
        for x in range(0, 6):
            media_pontos.append(int(len(self.btc)/math.pow(2, x)))
        return media_pontos


    def analise(self):
        self.btc = open("btcHistory.txt", "r").read().split(" ")
        self.btc = list(map(float, self.btc))
        num_pontos = self.media_de_pontos()
        lista_rs = [] #holds the value of "rs" for each division.
        media_valor = 0
        for i in range(1, 6): #This for runs through all possibel divisions of the values (divide in 1, in 2, in 4, in 8...)
            for j in range(0, int(math.pow(2,i))): #This one iterates over all n divisions
                rs = 0
                media_valor = 0
                desvio_aux = 0
                deviation_square = 0
                desvios = []

                # Iterates over all values inside a division, and it calculates de sum of all btc values
                for k in range(0, num_pontos[i]): 
                    l = k + j*num_pontos[i] #this 'l' is used because on each division I have to continue from where i finished the las one.
                    media_valor += self.btc[l] #1. Calculate the mean
                media_valor = media_valor/num_pontos[i] #the mean inside each division

                # the same as the last for, but this time it calculates the standard deviation
                for k in range(0, num_pontos[i]): 
                    l = k + j*num_pontos[i]
                    desvio_aux += self.btc[l]-media_valor # 3. Calculate the cumulative deviantions
                    deviation_square += math.pow(self.btc[l]-media_valor, 2) # Sum of squared deviantions, to calculate the standard deviantion
                    desvios.append(desvio_aux) #I did a list of of all mean deviations so I can call "max" and "min" functions afte
               
                rt = max(desvios)-min(desvios)
                standard_deviation = math.sqrt(deviation_square/num_pontos[i])
                rs += (rt/standard_deviation)
            rs = rs/(math.pow(2, i))
            lista_rs.append(math.log10(rs))

        num_pontos.pop(0)
        pontos_log = []
        for x in num_pontos:
            pontos_log.append(math.log10(x))

        x = np.array(pontos_log).reshape(-1,1)

        model = LinearRegression()
        model.fit(x, lista_rs)

        plt.scatter(x, lista_rs, color='r')
        plt.plot(x, model.predict(x),color='k')
        slope, intercept = np.polyfit(pontos_log, lista_rs, 1)
        plt.axis([-1.5, 3, -1.5, 3])
        plt.ylabel("Log R/S")
        plt.xlabel("Log size")
        plt.title(slope)
        plt.show()





if __name__ == "__main__":
    AnaliseRS().analise()
