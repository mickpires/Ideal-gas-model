class teste():
    def __init__(self,velocity=2):
        self.velocity = velocity

    def mudar(self,objeto):
        objeto.velocity = 3

a= teste()
print(f'velocidade antes da função: {a.velocity}')
a.mudar(a)
print(f'velocidade depois da função: {a.velocity}')
