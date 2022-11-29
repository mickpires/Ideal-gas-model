from particle import Particle
import numpy as np
#from scipy.stats import maxwell_gen
#TODO: implementar os negócios de pressão da parede 
class Space:
    def __init__(self,Np=3,x=10,y=10,dt=1,initial_velocity=1):
        self.Np = Np
        self.x = x
        self.y = y
        self.dt = dt
        self.time = 0
        self.particles = [Particle(id=i,dt=self.dt,velocity=self.giveVelocity(initial_velocity),position=self.givePosition()) for i in range(self.Np)]

    def create(self):
        possible_positions = np.linspace(-self.x-1,self.x-1,self.Np)
        possible_velocities = np.linspace(0,2*np.pi,self.Np)
        for particle in self.particles:
            particle.position = np.array(np.random.choice(possible_positions,size=(1,2),replace=False)).flatten()
            #print(f'posição da particula {particle.position}')

            # if particle.id == 1:
            #     particle.position = np.array([1,0])
            #     particle.velocity = np.array([-1,-1])
        for particle in self.particles:
            particle.velocity = np.array(np.random.choice(possible_velocities,size=(1,2),replace=True)).flatten()

    def givePosition(self):
        possible_positions = np.linspace(-self.x-1,self.x-1,self.Np)
        return np.array(np.random.choice(possible_positions,size=(1,2),replace=False)).flatten()

    def giveVelocity(self,initial_velocity):
        possible_angles = np.linspace(0,2*np.pi,self.Np)
        return np.array([initial_velocity * np.cos(np.random.choice(possible_angles)),initial_velocity * np.sin(np.random.choice(possible_angles))]).flatten()