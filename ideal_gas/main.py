from simulation import Simulation
import matplotlib.pyplot as plt
#Corrigir o problema da pressão. Tá calculando errado

simulation = Simulation(Np=2)
exe = 0
tempo = 30 #inserir um input depois
print(f'execução número {exe}')
while tempo > simulation.time:
    print('---------------------')
    exe += 1
    print(f'execução número {exe}')
    simulation.mainloop()
print(f'as pressões na simulação foram {simulation.pressures}')

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