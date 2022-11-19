from Particle import Particle
import numpy as np

class Space():
    def __init__(self,Np=3,x=10,y=10,dt=1):
        self.Np = Np
        self.particles = [Particle(i) for i in range(self.Np)]
        self.x = x
        self.y = y
        self.dt = dt
        self.space = np.zeros((self.x,self.y),dtype=object)
        self.create()

    def create(self):
        for particle in self.particles:
            if particle.id == 1:
                particle.position = np.array([9,9])
                particle.velocity *= -1
                particle.symbol = 'y'
            if particle.id == 2:
                particle.position = np.array([4,0])
                particle.velocity = np.array([0,1])
                particle.symbol  = 'z'
            y,x = particle.position
            self.space[y][x] = particle.symbol

    def move(self):
        for particle in self.particles:
            particle.path.append(particle.position)
            y,x = particle.position
            self.space[y][x] = 0
            particle.pos_position = particle.position + particle.velocity * self.dt
            y,x = particle.pos_position
            self.checkCollisionWall(particle,y,x)
            self.checkPath(particle)
        self.checkCollision() #isso tem que estar fora do for
        for particle in self.particles:
            particle.position = particle.pos_position
            y,x = particle.position
            self.space[y][x] = particle.symbol
            print(f'A particula {particle.id} andou nesse loop: {particle.path}')
            particle.path.clear()

    def checkCollisionWall(self,particle:Particle,y:int,x:int):
        if x < 0 or x > self.x-1:
            particle.velocity[1] *= -1
            particle.pos_position[1] = particle.position[1] + particle.velocity[1] *self.dt
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
        particles_id = []
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1.id == particle2.id:
                    continue
                for i in particle1.path:
                    for j in particle2.path:
                        if np.array_equal(i,j) and particle2.id not in particles_id:
                            print(f'A particula {particle1.id} e a particula {particle2.id} colidiram')
                            #A colisão provavelmente vai ser adicionada na linha de cima
                            particles_id.append(particle2.id)
                            particles_id.append(particle1.id)
    
    def collision(self,particle1,particle2): #TODO: Implementar colisão entre partículas
        pass
