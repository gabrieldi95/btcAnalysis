import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math

class AnaliseRS:

    #Primeiro pegar a média de pontos em cada intervalo
    def mediaDePontos(self):
        mediaPontos = []
        for x in range(0,6):
            mediaPontos.append( int(len(self.btc)/math.pow(2, x)) )
        return mediaPontos

    def analise(self):
        self.btc = open("btcHistory.txt", "r").read().split(" ")
        self.btc = list(map(float, self.btc))
        nroPontos = self.mediaDePontos()
        listaRS = [] #irá conter p rs de cada divisão
        mediaValor = 0
        for i in range(0,6):
            rs = 0
            for j in range(0, int(math.pow(2,i)) ):
                mediaValor = 0
                desvios = []
                for k in range(0,nroPontos[i]):
                    l = k + j*nroPontos[i]
                    mediaValor += self.btc[l]

                mediaValor = mediaValor/nroPontos[i]
                for k in range(0,nroPontos[i]):
                    desvioAux = 0
                    l = k + j*nroPontos[i]
                    desvioAux += self.btc[l]-mediaValor #vai somando todos os desvios
                    desvios.append(self.btc[l]-mediaValor)

                rt = max(desvios)-min(desvios)
                desvioPadrao = math.sqrt(math.pow(desvioAux, 2)/nroPontos[i])

            rs += (rt/desvioPadrao)/math.pow(2,i)
            listaRS.append(math.log10(rs))

        pontosLog = []
        for x in nroPontos:
            pontosLog.append(math.log10(x))

        x = np.array(pontosLog).reshape(-1,1)

        model = LinearRegression()
        model.fit(x, listaRS)

        plt.scatter(x, listaRS, color='r')
        plt.plot(x, model.predict(x),color='k')
        plt.show()





if __name__ == "__main__":
    AnaliseRS().analise()
