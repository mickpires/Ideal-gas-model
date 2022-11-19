from Space import Space
#TODO: Implementar colisão entre partículas

a = Space()
exe = 0
print(f'execução número {exe}')
print(a.space)
for i in range(11):
    print('---------------------')
    exe += 1
    print(f'execução número {exe}')
    a.move()
    print(a.space)