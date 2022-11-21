from simulation import Simulation
import matplotlib.pyplot as plt
#TODO: corrigir o o problema da pressão.
#TODO: generalizar o método de gerar partículas no espaço
#TODO: generalizar a criação do espaço para diferentes dt
#TODO:

simulation = Simulation(Np=3)
exe = 0
tempo = 60 #inserir um input depois
print(f'execução número {exe}')
print(simulation.space)
while tempo > simulation.time:
    print('---------------------')
    exe += 1
    print(f'execução número {exe}')
    simulation.mainloop()
    print(simulation.space)
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