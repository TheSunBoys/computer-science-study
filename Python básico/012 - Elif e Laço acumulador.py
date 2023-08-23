#ELIF
print("\_____________________________________________________________________________")
print('\nelif - Funciona como uma "terceira ou mais condicional" dentro de um bloco com if.')

print("\nExemplo do funcionamento de elif: \n")

texto = '''if temperatura <= 20:
    print("Tá muito frio.")
elif 20 < temperatura <= 25:
    print("Tá um pouco frio.")
elif 25 < temperatura <= 30:
    print("Temperatura estável")
elif 30 < temperatura <= 35:
    print("Tá quente viu.")
elif temperatura > 35:
    print("Literalmente Mossoró.")'''

print(texto)

#LAÇO ACUMULADOR
print("\n_____________________________________________________________________________")

print("\nLAÇO ACUMULADOR DE SOMA:")

lista = [4, 5, -1, 12, 8]
soma = 0

for i in lista:
    soma = soma + i

texto1 = '''lista = [4, 5, -1, 12, 8]
soma = 0

for i in lista:
    soma = soma + i'''

print("\n" + texto1)

print("\nSoma dos valores da lista = ", soma)    

print("\nLAÇO ACUMULADOR DE MULTIPLICAÇÃO:")

lista = [4, 5, -1, 12, 8]
multiplicação = 1

for j in lista:
    multiplicação = multiplicação * j

texto2 = '''lista = [4, 5, -1, 12, 8]
multiplicação = 1

for i in lista:
    multiplicação = multiplicação * i'''

print("\n"+ texto2)

print("\nMultiplicação dos valores da lista = ", multiplicação)    

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")