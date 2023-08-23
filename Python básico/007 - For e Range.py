#FOR E RANGE
print("_____________________________________________________________________________")

print("\nFOR - É um laço de repetição, aqui está um exemplo do uso dele: ")

print("\nfor x in name:")
print("     print(x)")

print("\nx - é uma variável criada para o laço for")
print("name - pode ser qualquer coisa, uma string, uma lista, etc.")

lista = [1, 3, 5, 7, 11, 13]
nome = "batata"

print("\nFor em uma lista:")
for x in lista:
    print(x)

print("\nFor em uma string:")
for y in nome:
    print(y)

print("\n_____________________________________________________________________________")

print("RANGE - Normalmente utilizado junto com o laço for e é usado para criar uma sequência de inteiros")

print("\nrange(n) - Sequência de n valores começando do 0")
print("range(início, fim) - Sequência de números começando de início e terminando antes do fim")
print("range(início, fim, passo) - Sequência de números começando de início e terminando antes do fim, somando passo valores")

print("\nfor a in range(6):")
for a in range(6):
    print(a)

print("\nfor b in range(1, 6):")
for b in range(1, 6):
    print(b)

print("\nfor c in range(0, 10, 2):")
for c in range(0, 10, 2):
    print(c)
    
print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")