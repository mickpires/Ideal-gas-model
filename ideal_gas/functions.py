import numpy as np
from pandas import DataFrame

def magnitude(a):
        value = 0
        for i in a:
            value += i**2
        return np.sqrt(value)

def sturges(dataframe:DataFrame): #número de classes
    return int(np.ceil(1 + 3.3 * np.log(len(dataframe))))

def limiteClasses(value,sturges):
    amplitude_total = value[-1] - value[0]
    amplitude_intervalo_classe = amplitude_total / sturges
    limite_inferior = value[0]
    limites = [limite_inferior]
    while limite_inferior <= value[-1]:
        limite_superior = amplitude_intervalo_classe + limite_inferior
        limites.append(limite_superior)
        limite_inferior = limite_superior
    
    return limites