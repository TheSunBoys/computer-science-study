#PROGRAMAÇÃO ORIENTADA À OBJETOS 01
print("_____________________________________________________________________________")

print('''POO - Programação Orientada a Objetos é um paradigma de programação que se
baseia no conceito de objetos, que são entidades que possuem características
(atributos) e comportamentos(métodos). Os objetos que interagem entre si através
de mensagens.

CLASSES - Define as características e comportamentos que os objetos terão. Uma classe
é como um modelo a partir do qual os objetos são criados.

EXEMPLO DE UMA CLASSE POINT: ''')

class Point:
    'classe que representa dois pontos em um plano cartesiano'
    def definir_x(self, coordx):
        'define a coordenada x do ponto como coordx'
        self.x = coordx

    def definir_y(self, coordy):
        'define a coordenada y do ponto como coordy'
        self.y = coordy

    def mostrar(self):
        'mostra o ponto x e o ponto y do objeto em uma tupla'
        return(self.x, self.y)
    
    def mover(self, dx, dy):
        'move as coordenadas de x e y tomando dx e dy com distância'
        self.x += dx
        self.y += dy

classe_ponto = '''\nclass Point:
    'classe que representa dois pontos em um plano cartesiano'
    def definir_x(self, coordx):
        'define a coordenada x do ponto como coordx'
        self.x = coordx

    def definir_y(self, coordy):
        'define a coordenada y do ponto como coordy'
        self.y = coordy

    def mostrar(self):
        'mostra o ponto x e o ponto y do objeto em uma tupla'
        return(self.x, self.y)
    
    def mover(self, dx, dy):
        'move as coordenadas de x e y tomando dx e dy com distância'
        self.x += dx
        self.y += dy'''

print(classe_ponto)    

print('''\nself -  é utilizado para referenciar o OBJETO que está sendo manipulado dentro
de uma classe. Ele é utilizado em métodos de INSTÂNCIA, ou seja, métodos que são associados
a uma instância específica da classe.''')

print("\n_____________________________________________________________________________")

ponto = Point()
ponto.definir_x(2)
ponto.definir_y(4)

print('''\nCRIANDO UM OBJETO POINT:

ponto = Point()

(Aqui estamos dizendo que ponto é um objeto da classe point)

DEFININDO X E Y:

ponto.definir_x(2)
ponto.definir_y(4)

(Aqui estamos utilizando os métodos definir_x e definir_y) para definir os valores x e y do objeto ponto)

VEJA O VALOR DE X E Y DO OBJETO PONTO:

ponto.x = {0}
ponto.y = {1}'''.format(ponto.x, ponto.y, ponto.mostrar()))

print("\nOUTRAS FUNÇÕES:\n\nponto.mostrar() --> {0}".format(ponto.mostrar()))
ponto.mover(4, 4)
print("\nponto.mover(4, 4)\nponto.x = {0}\nponto.y = {1}". format(ponto.x, ponto.y))

print("\n_____________________________________________________________________________")

print('''
IMPORTANTE VISUALIZAR:

dir(Point)
{0}

dir(ponto)
{1}'''.format(dir(Point), dir(ponto)))

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")