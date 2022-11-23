from particle import Particle
import numpy as np
from functions import *
#TODO: implementar os negócios de pressão da parede 
class Space():
    def __init__(self,Np=3,x=10,y=10,dt=1):
        self.Np = Np
        self.x = x
        self.y = y
        self.dt = dt
        self.time = 0
        self.particles = [Particle(id=i,dt=self.dt) for i in range(self.Np)]
        self.space = np.zeros((self.x,self.y),dtype=object)
        self.create()

    def create(self):
        for particle in self.particles:
            if particle.id == 1:
                particle.position = np.array([1,0])
                particle.velocity = np.array([0,-1])
                particle.symbol = 'y'
            if particle.id == 2:
                particle.position = np.array([4,0])
                particle.velocity = np.array([0,1])
                particle.symbol  = 'z'
            y,x = particle.position
            self.space[y][x] = particle.symbol
