import numpy as np

#TODO: Implementar colisão entre partículas

class Particle():                          #y,x
    def __init__(self,id,velocity=np.array([1,1]),position=np.array([0,0])):
        self.id = id
        self.velocity_x = velocity[1]
        self.velocity_y = velocity[0]
        self.velocity = np.array([self.velocity_y,self.velocity_x])
        self.position = position
        self.pos_position = np.zeros((1,2))
        self.symbol = 'x'
        self.path = []