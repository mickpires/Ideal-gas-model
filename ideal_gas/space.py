from particle import Particle
import numpy as np
#TODO: implementar os negócios de pressão da parede 
class Space():
    def __init__(self,Np=3,x=10,y=10,dt=1):
        self.Np = Np
        self.x = x
        self.y = y
        self.dt = dt
        self.time = 0
        self.time_wall_collision = []
        self.particles = [Particle(id=i,dt=self.dt) for i in range(self.Np)]
        self.space = np.zeros((self.x,self.y),dtype=object)
        self.pressures = []
        self.did_collide_wall = False
        self.wall_vector = np.array([0,self.x]) #vetor da parede que detecto a pressão
        self.forces = []
        self.create()

    def mainloop(self):
        self.time += self.dt
        for particle in self.particles:
            y,x = particle.position
            self.space[int(y)][int(x)] = 0
            self.euler(particle)
        self.checkCollision()
        for particle in self.particles:
            particle.position = particle.pos_position
            y,x = particle.position
            self.space[int(round(y))][int(round(x))] = particle.symbol
            print(f'A particula {particle.id} andou nesse loop: {particle.path}')
            particle.path.clear()
        print(f'A parede foi colidida? {self.did_collide_wall}')
        if self.did_collide_wall:                                
            self.checkPressure()

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
                            np.absolute(self.magnitude((particle1_initial_velocity - \
                                particle2_initial_velocity)*self.dt))**2)

        particle2.velocity = particle2_initial_velocity - 2* particle1.mass * \
            np.dot(particle2_initial_velocity - \
                particle1_initial_velocity, (particle2_initial_velocity-particle1_initial_velocity)*self.dt) * \
                    (particle2_initial_velocity-particle1_initial_velocity)*self.dt / \
                        ((particle2.mass + particle1.mass) * \
                            np.absolute(self.magnitude(particle2_initial_velocity - \
                                particle1_initial_velocity)*self.dt)**2)
        
        particle1.velocity = self.toInt(particle1.velocity)
        particle2.velocity = self.toInt(particle2.velocity)

    def euler(self,particle:Particle):
        particle.path.clear()
        particle.path.append(particle.position)
        particle.pos_position = particle.position + particle.velocity * self.dt
        y,x = particle.pos_position
        self.checkCollisionWall(particle,y,x)
        self.checkPath(particle)

    def magnitude(self,a):
        value = 0
        for i in a:
            value += i**2
        return np.sqrt(value)

    def toInt(self,a):
        velocity = np.array([0,0])
        for i in range(len(a)):
            velocity[i] = round(a[i])
        return velocity

    def checkPressure(self):
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
        self.forces.clear()
        self.pressures.append(pressure)
        self.time_wall_collision.append(self.time)