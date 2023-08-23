print("\n_____________________________________________________________________________")

print('''SET - Um objeto set é uma coleção de elementos únicos e não ordenados. Isso significa
que um set NÃO pode conter elementos duplicados, ele também REORDENA os elementos.''')

print("\nOBJETOS DA CLASSE SET SÃO DELIMITADAS POR CHAVES:")

print("\nconjunto1 = {1, 2, 4, 5, 5, 3}")
conjunto1 = {1, 2, 4, 5, 5, 3}
print("conjunto1 -->", conjunto1)

print("\nÉ POSSÍVEL USAR ELE PARA REMOVER DUPLICATAS DE UMA LISTA:")

print("\nlista = [23, 19, 18, 21, 18, 20, 21, 23, 22, 23, 19, 20]")
lista = [23, 19, 18, 21, 18, 20, 21, 23, 22, 23, 19, 20]
print("lista = list(set(lista))")
lista = list(set(lista))
print("lista -->", lista)

print("_____________________________________________________________________________")
print("OPERAÇÕES COM SET")

print("\nFora os operadores lógicos báscios (in, not in, ==, !=, <, <=), também temos:")

conjuntoI = {1, 2, 3, 4, 5}
conjuntoII = {4, 5, 6, 7, 8}

print('''\nconjuntoI = {1, 2, 3, 4, 5}
conjuntoII = {4, 5, 6, 7, 8}''')

print("\nUNIÃO( | ) - Une os elementos de cada objeto set.")
print("conjutoI | conjuntoII -->", conjuntoI | conjuntoII)

print("\nINTERSEÇÃO( & ) - Elementos em comum dos dois objetos set.")
print("conjutoI & conjuntoII -->", conjuntoI & conjuntoII)

print("\nDIFERENÇA( - ) - Oque tem no conjuntoI e não tem no conjuntoII.")
print("conjutoI - conjuntoII -->", conjuntoI - conjuntoII)

print("\nDIFERENÇA( ^ ) - Elementos tem no conjuntoI ou no conjuntoII, mas NÃO EM AMBOS")
print("conjutoI ^ conjuntoII -->", conjuntoI ^ conjuntoII)

print("\n_____________________________________________________________________________")
print("MÉTODOS COM SET")

print("\nnomes = {'Pedro', 4, 'Ana', 'Paula', 'Jorge'}")
nomes = {'Pedro', 4, 'Ana', 'Paula', 'Jorge'}

nomes.add('Patrícia')
print("\nnomes.add('Patrícia') - Adiciona um elemento ao conjunto.")
print("nomes -->", nomes)

nomes.remove(4)
print("\nnomes.remove(4) - Remove um elemento do conjunto.")
print("nomes -->", nomes)

nomes.clear()
print("\nnomes.clear() - Apaga todos os elementos do conjunto.")
print("nomes -->", nomes)

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")