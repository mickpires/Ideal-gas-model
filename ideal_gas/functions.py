import numpy as np

def magnitude(a):
        value = 0
        for i in a:
            value += i**2
        return np.sqrt(value)