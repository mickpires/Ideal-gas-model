from collision import Collision
from particle import Particle
import numpy as np

class Simulation(Collision):
    def __init__(self, Np=3, x=10, y=10, dt=1):
        super().__init__(Np, x, y, dt)
        self.time_wall_collision = []
        self.pressures = []
        self.wall_vector = np.array([[0,self.x]]) #vetor da parede que detecto a pressão
        self.forces = np.array([[]])

    def mainloop(self):
        self.time += self.dt
        for particle in self.particles:
            #self.space[int(y)][int(x)] = 0
            self.euler(particle)
        self.checkCollision()
        for particle in self.particles:
            particle.position = particle.pos_position
            #self.space[int(round(y))][int(round(x))] = particle.symbol
            print(f'A particula {particle.id} andou nesse loop: {particle.path}')
            particle.path = np.array([[]])
        print(f'A parede foi colidida? {self.did_collide_wall}')
        if self.did_collide_wall:                                
            self.checkPressure()

    def checkPressure(self): # não está calculando. Arrumar
        total_force = 0
        for forces in self.forces:
            total_force += np.absolute(forces) #{Talvez aqui dê problema. Talvez o correto fosse aplicar o modulo aqui}
        total_force = total_force / len(self.forces)
        pressure = np.dot(total_force,self.wall_vector)
        print(f"O comprimento da array self.forces é {self.forces}")
        print(f'A força total é {total_force}')
        print(f'A pressão na parede é {pressure}')
        print(f'As forças que colidiram na parede: {self.forces}')
        self.did_collide_wall = False
        self.forces = np.array([[]])
        self.pressures.append(pressure)
        self.time_wall_collision.append(self.time)


    def euler(self,particle:Particle):
        particle.path = np.array([particle.position])
        particle.pos_position = particle.position + particle.velocity * self.dt
        x,y = particle.pos_position
        self.checkCollisionWall(particle,x,y)
        self.checkPath(particle)