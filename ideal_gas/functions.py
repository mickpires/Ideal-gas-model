import numpy as np

def magnitude(a):
        value = 0
        for i in a:
            value += i**2
        return np.sqrt(value)

def toInt(a):
    velocity = np.array([0,0])
    for i in range(len(a)):
        velocity[i] = round(a[i])
    return velocity