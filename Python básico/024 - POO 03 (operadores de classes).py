print("_____________________________________________________________________________")

class Point:
    def __init__(self, coordx = 0, coordy = 0):
        self.x = coordx
        self.y = coordy

ponto = Point(2, 4)      

class Gato:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 

    def __repr__(self):
        gatinho = '(Nome: {0}, Cor: {1})'.format(self.nome, self.cor)  
        return gatinho   

gato1 = Gato('Alfred', 'cinza')

print('''
Por um objeto ponto = Point(2, 4) se tratar justamente de um objeto do tipo Point, temos
algumas incoveniências:

print(ponto): 
{0}

len(ponto):
{1}

Portando, é importante definir essas funções básicas como métodos dessa classe, afinal
até os operadores mais básicos são métodos:

x + y    -->   x.__add__(y)
x - y    -->   x.__sub__(y)
x * y    -->   x.__mul__(y)
x / y    -->   x.__truediv__(y)
repr(x)  -->   x.__repr__() 

E podemos fazer o mesmo com as classes, vamos criar uma classe Gato como exemplo:

class Gato:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor 

    def __repr__(self):
        gatinho = '(Nome: { 0 }, Cor: { 1 })'.format(self.nome, self.cor)  
        return gatinho   

gato1 = Gato('Alfred', 'cinza')

print(gato1) --> {2}

'''. format(ponto, TypeError, gato1)) 

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")