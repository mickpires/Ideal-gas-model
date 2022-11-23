from space import Space
from particle import Particle
import numpy as np
from functions import *

class Collision(Space):
    def __init__(self, Np=3, x=10, y=10, dt=1):
        super().__init__(Np, x, y, dt)
        self.did_collide_wall = False

    def checkCollisionWall(self,particle:Particle,x:int,y:int):
        #print(f'posição da particula {particle.pos_position}')
        if x < 0 or x > self.x-1: 
            particle.velocity[0] *= -1
            if x < 0:
                self.did_collide_wall = True
                self.forces = np.vstack(particle.force())
                particle.pos_position[0] = 0
            elif x > self.x-1:
                particle.pos_position[0] = self.x-1
        if y < 0 or y > self.y-1:
            particle.velocity[1] *= -1
            if y < 0:
                particle.pos_position[1] = 0
            elif y > self.y-1:
                particle.pos_position[1] = self.y-1
    
    def checkPath(self,particle:Particle): #implementar o que está escrito no arquivo teste aqui
            num_pontos = 2
            x = np.linspace(particle.position[0],particle.pos_position[0],num_pontos)
            y = np.linspace(particle.position[1],particle.pos_position[1],num_pontos)
            for i in range(num_pontos):
                particle.path = np.vstack((particle.path,[[x[i],y[i]]]))

    def checkCollision(self):
        ignore_list = []
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1.id == particle2.id:
                    continue
                for i in particle1.path:
                    for j in particle2.path:
                        if np.array_equal(i,j) and particle2.id not in ignore_list and not np.array_equal(particle1.velocity,particle2.velocity):
                            #print(f'A particula {particle1.id} e a particula {particle2.id} colidiram')
                            self.collision(particle1,particle2)
                            #print(f'velocidade da particula 1: {particle1.velocity}')
                            #print(f'velocidade da particula 2: {particle2.velocity}')
                            for particle in (particle1,particle2):
                                    self.euler(particle)
                                    ignore_list.append(particle.id)
                                    ignore_list.append(particle.id)
    
    def collision(self,particle1:Particle,particle2:Particle):
        particle1_initial_velocity = particle1.velocity
        particle2_initial_velocity = particle2.velocity
        particle1.velocity = particle1_initial_velocity - 2*particle2.mass * \
            np.dot(particle1_initial_velocity - \
                particle2_initial_velocity,(particle1_initial_velocity - particle2_initial_velocity)*self.dt) * \
                    (particle1_initial_velocity-particle2_initial_velocity)*self.dt / \
                        ((particle1.mass + particle2.mass) * \
                            np.absolute(magnitude((particle1_initial_velocity - \
                                particle2_initial_velocity)*self.dt))**2)

        particle2.velocity = particle2_initial_velocity - 2* particle1.mass * \
            np.dot(particle2_initial_velocity - \
                particle1_initial_velocity, (particle2_initial_velocity-particle1_initial_velocity)*self.dt) * \
                    (particle2_initial_velocity-particle1_initial_velocity)*self.dt / \
                        ((particle2.mass + particle1.mass) * \
                            np.absolute(magnitude(particle2_initial_velocity - \
                                particle1_initial_velocity)*self.dt)**2)