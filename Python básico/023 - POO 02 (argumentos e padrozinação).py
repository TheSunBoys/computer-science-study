#PROGRAMAÇÃO ORIENTADA À OBJETOS 02
print("_____________________________________________________________________________")

print('''
CONSTRUTOR COM ARGUMENTOS DE ENTRADA - Para criar uma classe que recebe argumentos de entrada
temos que incluir o método "def __init__()", como necesse exemplo:

class Point:
    def __init__(self, coordx, coordy):
        self.x = coordx
        self.y = coordy

O método "def __init__()" obrigatoriamente deve possuir o self, o número de argumentos pode
ser quantos quisermos. Mas lembre-se que agora a criação de objetos Point só funcionam se
receberem dois argumentos, caso contrário:

ponto = Point() --> {0}
'''.format(TypeError))
print("\n_____________________________________________________________________________")

class Point:
    def __init__(self, coordx = 0, coordy = 0):
        self.x = coordx
        self.y = coordy

    def get (self):
        return (self.x, self.y)    

a = Point()
b = Point(3, 2)

print('''
CONSTRUTOR PADRÃO - Se quisermos fazer uma classe com argumentos PADRÕES, já podemos
declarar eles quando fizermos a Classe específica.

class Point:
    def __init__(self, coordx = 0, coordy = 0):
        self.x = coordx
        self.y = coordy

    def get (self):
        return (self.x, self.y) 
    
- Se não recebe nenhum argumento, o PADRÃO será: 
a = Point()
a.get() --> {0}

- Mas se recebe algum argumento:
b = Point(3, 2)
b.get() --> {1}'''.format(a.get(), b.get()))   

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")