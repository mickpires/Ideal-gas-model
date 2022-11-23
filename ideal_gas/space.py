from particle import Particle
import numpy as np
from functions import *
#from scipy.stats import maxwell_gen
from random import randint
#TODO: implementar os negócios de pressão da parede 
class Space:
    def __init__(self,Np=3,x=10,y=10,dt=1):
        self.Np = Np
        self.x = x
        self.y = y
        self.dt = dt
        self.time = 0
        self.particles = [Particle(id=i,dt=self.dt) for i in range(self.Np)]
        self.create()

    def create(self):
        for particle in self.particles:
            if particle.id == 1:
                particle.position = np.array([1,0])
                particle.velocity = np.array([-1,0])

    # def isThereSomethingAround(self,y,x):
    #     if self.space[y+1][x] == 0 and self.space[y-1][x] == 0 and self.space[y][x+1] == 0 and \
    #         self.space[y][x-1] == 0 and self.space[y+1][x+1] == 0 and self.space[y-1][x-1] == 0:
    #         return False
    #     else:
    #         return True

