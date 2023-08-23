#MÓDULO RANDOM
print("_____________________________________________________________________________")
import random

print("\nI - random.randrange(x, y) - Gera um valor aleátorio entre x (incluindo x) e y (não incluindo y).")

print("\nEscolhendo um int aleátorio entre 1 e 7:")

def randint():
    contador = 0
    while contador != 5:
        num = random.randrange(1,7)
        contador += 1
        print(num) 

randint()

print("\nII - random.uniform(x, y) - Gera um valor aleátorio n do tipo float de modo que x <= n <= y.")

print("\nEscolhendo um float aleátorio entre 1 e 2:")

def randfloat():
    contador = 0
    while contador != 5:
        num = random.uniform(1,2)
        contador += 1
        print(num) 

randfloat()

print("\nIII - random.choice(list) - Escolhe de forma aleatória um item do contêiner list.")

print("\nlista = ['maça', 'banana', 'uva', 'abacaxi', 'laranja', 'ameixa', 'pera', 'pêssego']")
lista = ['maça', 'banana', 'uva', 'abacaxi', 'laranja', 'ameixa', 'pera', 'pêssego']

print("\nEscolhendo um item aleátorio de lista:")

def randstring(list):
    contador = 0
    while contador != 5:
        item = random.choice(list)
        contador += 1
        print(item) 

randstring(lista)

print("\nIV - random.sample(list, k) - Fornece uma amostra aleátoria do contêiner list com k itens.")

print("\nlista = ['maça', 'banana', 'uva', 'abacaxi', 'laranja', 'ameixa', 'pera', 'pêssego']")
lista = ['maça', 'banana', 'uva', 'abacaxi', 'laranja', 'ameixa', 'pera', 'pêssego']

print("\nEscolhendo 3 itens aleátorios da lista:")

def randsample(list):
    contador = 0
    while contador != 5:
        item = random.sample(list, 3)
        contador += 1
        print(item) 

randsample(lista)

print("\nV - random.shuffle(list) - Embaralha os itens do contêiner list.")

print("\nvalores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nrandom.shuffle(valores) -->", random.shuffle(valores))
print("random.shuffle(valores) -->", random.shuffle(valores))
print("random.shuffle(valores) -->", random.shuffle(valores))

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")