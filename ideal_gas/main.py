from simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
#Ver qualé da merda do gerador aleatorio
#tá dando o mesmo erro daquela vez na parte da colisão. basicamente as velocidades das particulas
#estão iguais. O que não faz sentido elas colidirem então
#arrumar o tempo

simulation = Simulation(Np=50,dt=1e-2)
exe = 0
tempo = 2 #inserir um input depois
#print(f'execução número {exe}')
while tempo > simulation.time: #acho que está errado esse simulation.time
    print(f'tempo na simulação: {simulation.time}')
    print('-' * 60)
    exe += 1
    print(f'execução número {exe}')
    simulation.mainloop()
#print(f'as pressões na simulação foram {simulation.pressures}')
#print(f'Os tempos das colisões na simulação foram {simulation.time_wall_collision}')
print(f'o desvio padrão da pressão {np.std(simulation.pressures)}')

plt.plot(simulation.time_wall_collision,simulation.pressures)
plt.title('Como podemos ver, fudeu')
plt.xlabel('Tempo (s)')
plt.ylabel('Pressão (Pa)')
plt.ylim(-0.005,0.005)
plt.show()
plt.close()
#scatter
plt.scatter(simulation.time_wall_collision,simulation.pressures)
plt.title('Como podemos ver, fudeu')
plt.xlabel('Tempo (s)')
plt.ylabel('Pressão (Pa)')
plt.ylim(-0.005,0.005)
plt.show()
plt.close()

#graficos do número de particulas vs a velocidade