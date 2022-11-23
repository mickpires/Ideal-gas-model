from simulation import Simulation
import matplotlib.pyplot as plt
#Ver qualé da merda do gerador aleatorio
#tá dando o mesmo erro daquela vez na parte da colisão. basicamente as velocidades das particulas
#estão iguais. O que não faz sentido elas colidirem então

simulation = Simulation(Np=100)
exe = 0
tempo = 60 #inserir um input depois
print(f'execução número {exe}')
while tempo > simulation.time:
    print('---------------------')
    exe += 1
    print(f'execução número {exe}')
    simulation.mainloop()
print(f'as pressões na simulação foram {simulation.pressures}')
print(f'Os tempos das colisões na simulação foram {simulation.time_wall_collision}')

plt.plot(simulation.time_wall_collision,simulation.pressures)
plt.title('Como podemos ver, fudeu')
plt.xlabel('Tempo (s)')
plt.ylabel('Pressão (não sei unidade de pressão, é mole KKKKKKKKKKKKKK)')
plt.show()
plt.close()
plt.scatter(simulation.time_wall_collision,simulation.pressures)
plt.title('Como podemos ver, fudeu')
plt.xlabel('Tempo (s)')
plt.ylabel('Pressão (não sei unidade de pressão, é mole KKKKKKKKKKKKKK)')
plt.show()