from space import Space
from particle import Particle
import numpy as np
from functions import *

class Collision(Space):
    def __init__(self, Np=3, x=10, y=10, dt=1):
        super().__init__(Np, x, y, dt)
        self.did_collide_wall = False

    def checkCollisionWall(self,particle:Particle,y:int,x:int):
        if x < 0 or x > self.x-1:
            particle.velocity[1] *= -1
            particle.pos_position[1] = particle.position[1] + particle.velocity[1] *self.dt
            if x < 0:
                self.did_collide_wall = True
                self.forces.append(particle.force())
        if y < 0 or y > self.y-1:
            particle.velocity[0] *= -1
            particle.pos_position[0] = particle.position[0] + particle.velocity[0] *self.dt
    
    def checkPath(self,particle:Particle):
        path = particle.position.copy()
        while path[0] != particle.pos_position[0] or path[1] != particle.pos_position[1]:
            if particle.velocity[1] < 0:
                path[1]-= 1
            elif particle.velocity[1] > 0:
                path[1] += 1
            if particle.velocity[0] < 0:
                path[0] -= 1
            elif particle.velocity[0] > 0:
                path[0] += 1
            p = path.copy()
            particle.path.append(p)

    def checkCollision(self):
        ignore_list = []
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1.id == particle2.id:
                    continue
                for i in particle1.path:
                    for j in particle2.path:
                        if np.array_equal(i,j) and particle2.id not in ignore_list:
                            print(f'A particula {particle1.id} e a particula {particle2.id} colidiram')
                            self.collision(particle1,particle2)
                            print(f'velocidade da particula 1: {particle1.velocity}')
                            print(f'velocidade da particula 2: {particle2.velocity}')
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
        
        particle1.velocity = toInt(particle1.velocity)
        particle2.velocity = toInt(particle2.velocity)