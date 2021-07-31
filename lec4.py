import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import random
import statsmodels.api as sm
from scipy.special import gamma

def lanzamientos(n):
    medias = []
    for i in range(100000):
        muestras = np.random.normal(21.72, 2.3, n)
        medias.append(np.mean(muestras))
    return medias
    
# 3.1.b

muestras20 = lanzamientos(20)
#media = np.mean(muestras20)
#desviacionEstandar = np.std(muestras20)

# 3.1.c

def graficos():
    x = np.linspace(20, 30, 100)
    plt.hist(muestras20, bins = round((max(muestras20) - min(muestras20))/((2*(np.percentile(muestras20, 75) - np.percentile(muestras20,25)))/10)), density = True, color='#1800B2')
    plt.savefig(str(20) + "muestras.png")
    plt.show()
    plt.clf()

    muestras40 = lanzamientos(40)
    plt.hist(muestras40, bins = round((max(muestras40) - min(muestras40))/((2*(np.percentile(muestras40, 75) - np.percentile(muestras40,25)))/10)), density = True, color='#1800B2')
    plt.savefig(str(40) + "muestras.png")
    plt.show()
    plt.clf()

graficos()
