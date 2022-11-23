import numpy as np

class Particle:                          
    def __init__(self,id,velocity=np.array([1,0]),position=np.array([0,0]),mass=1e-3,radius = 1e-2,dt=1):
        self.id = id
        self.velocity_x = velocity[1]
        self.velocity_y = velocity[0]
        self.velocity = np.array([self.velocity_y,self.velocity_x])
        self.position = position
        self.radius = radius
        self.mass = mass
        self.pos_position = np.zeros((1,2))
        self.symbol = 'x'
        self.path = np.array([[]])
        self.dt = dt
    
    def force(self):
        self.momentum = self.mass * self.velocity
        force = self.momentum / self.dt
        return force