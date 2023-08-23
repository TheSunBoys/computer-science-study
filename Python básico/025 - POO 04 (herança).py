# HERANÇA DE CLASSES - Quando uma classe herda os atributos e métodos de outra classe. A classe que herda é conhecida como classe filha e a classe que teve seus atributos herdados é uma superclasse.

# Aqui temos uma classe Rocha 
class Rocha:

    def setnome(self):
        nome = input("NOME DA ROCHA: ")
        self.nome = nome

    def setcor(self):
        cor = input("COR DA ROCHA: ")
        self.cor = cor 

    def setdureza(self):
        dureza = input("DUREZA DA ROCHA: ")
        self.dureza = dureza

    def __repr__(self):
        atributos = '''
        Atributos da rocha {0} 
        Cor: {1} 
        Dureza: {2}
        '''.format(self.nome, self.cor, self.dureza)
        return atributos

# Aqui temos uma nova classe Cristal que herda atributos da superclasse Rocha
class Cristal(Rocha): 

# Com o diferencial que podemos adicionar outro método...     
    def setbrilho(self): 
        brilho = input("BRILHO DO CRISTAL: ")
        self.brilho = brilho

# Ou modificar um método já existente...
    def setcor(self):
        cor_cristal = input("COR DO CRISTAL: ")
        self.cor = cor_cristal

    def setdureza(self):
        dureza_cristal = input("DUREZA DO CRISTAL: ")
        self.dureza = dureza_cristal

    def __repr__(self):
        atributos = '''
        Atributos do cristal {0} 
        Cor: {1} 
        Dureza: {2}
        Brilho: {3}
        '''.format(self.nome, self.cor, self.dureza, self.brilho)
        return atributos    
# O mesmo vale pra atributos

rocha01 = Rocha()
rocha01.setnome()
rocha01.setcor()
rocha01.setdureza()
print(rocha01)

rocha02 = Cristal()
rocha02.setnome()
rocha02.setcor()
rocha02.setdureza()
rocha02.setbrilho()
print(rocha02)

input()

# Se sua classe se comporta como um Queue, também vale a pena conferir os operadores: 
# __getitem__()
# __setitem__()
# __iter__()