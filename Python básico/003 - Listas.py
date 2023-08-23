#LISTAS
print("_____________________________________________________________________________")

print("\nEm Python, listas são sequências de objetos, podendo esses serem números, strings ou outras listas.")

print("\nlista = ['um', 2, [3, 4]]")
lista = ['um', 2, [3, 4], 5.0]
print("\nlista1 = [1, 2, 3, 4]")
lista1 = [1, 2, 3, 4]
print("\nlista2 = ['dog, 'cat, 'fish']")
lista2 = ['dog', 'cat', 'fish']

print("\nDo mesmo modo que funcionam com strings, esse comandos também funcionam com listas: ")
print("\n1 - x in lst - Verifica se um item x está na lista")
print("2 - x not in lst - Verifica se um item x NÃO está na lista")
print("3 - lstA + lstB - Contatena duas listas")
print("4 - lst * n, n * lst - Contatena n cópias da lista list")
print("5 - lst[i] - Item da lista no índice i")
print("6 - len(lst) - Número de elementos que tem na lista")
print("7 - min(lst) - Menor item da lista (MENOR STRING OU MENOR NÚMERO DA LISTA)")
print("8 - max(lst) - Maior item da lista (MAIOR STRING OU MAIOR NÚMERO DA LISTA)")
print("9 - sum(lst) - Soma os itens da lista (PARA NÚMEROS)")

print("\n_____________________________________________________________________________")

print("\nMÉTODOS DE LISTA")
print("\nMétodos - Função associada a um objeto ou uma classe")
print("Argumentos - Valor ou variável passada para uma função")

print("\ncores = ['azul', 'vermelho', 'amarelo']")
cores = ['azul', 'vermelho', 'amarelo']

print("\nI - lst.append(item): Adiciona item ao final da lista")
print("\ncores.append('verde')")
print(cores)

print("\nII - lst.count(item): Retorna número de vezes que item aparece na lista")
print("\ncores.count('azul')")
print(cores.count('azul'), "- azul só aparece 1 vez na lista")

print("\nIII - lst.index(item): Retorna no índice da primeira ocorrência do item na lista")
print("\ncores.index('vermelho')")
print(cores.index('vermelho'), "- vermelho aparece no índice 1 da lista")

print("\nIV - lst.insert(índice, item): Insere item na lista antes de índice")
print("\ncores.insert(0, 'preto')")
cores.insert(0, 'preto')
print(cores)

print("\nV - lst.pop(): Remove o último item da lista, mas você pode escolher qual item, colocando o ÍNDICE COMO PARÂMETRO.")
print("\ncores.pop()")
cores.pop()
print(cores)

cores.append('amarelo')
print("\nVI - lst.remove(item): Remove a primeira ocorrência do item na lista")
print("\ncores.remove('preto')")
cores.remove('preto')
print(cores)

print("\nVII - lst.reverse(): Inverte a ordem dos itens na lista")
print("\ncores.reverse()")
cores.reverse()
print(cores)

print("\nVII - lst.sort(): é usado para ordenar os elementos de uma lista em ordem crescente")
print("NÚMEROS - Do menor para o maior")
print("STRINGS - Ordem alfabética")

print("\nnumeros = [5, 2, 8, 1, 9, 3]")
numeros = [5, 2, 8, 1, 9, 3]
numeros.sort()
print(numeros)

print("\nfrutas = ['banana', 'maçã', 'laranja', 'abacaxi']")
frutas = ['banana', 'maçã', 'laranja', 'abacaxi']
frutas.sort()
print(frutas)

print("\nVII - lst.sorted(): Mesma função do .sort(), mas NÃO modifica a lista")
print('numeros = [5, 2, 8, 1, 9, 3, 7, 12, 20]')
print('numeros_ordenados = sorted(numeros)')
numeros = [5, 2, 8, 1, 9, 3, 7, 12, 20]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
print(numeros)

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")