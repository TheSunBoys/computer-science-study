print("_____________________________________________________________________________")
#MÓDULOS
print('''\nNAMESPACES DE MÓDULOS - Os módulos, quando executados, são namespaces. É
justamente nos módulos que estão definidos os nomes de funções, valores e classes.''')

print("\nCOMANDO dir() - Serve para visualizar os atributos de um módulo.")
print('''\nimport math
dir(math)\n''')
import math
print(dir(math))

print("\n'__doc__', '__loader__', '__name__', '__package__', '__spec__'")
print('''(Esses são módulos que existem para cada modulo importado, são definidos pelo
interpretador no momento que o módulo é importando para fins de manutenção''')

print("\n_____________________________________________________________________________")

print('''\nQUANDO UM INTERPRETRADOR EXECUTA(IMPORTA) UM MÓDULO:
1) Procura o arquivo do módulo;
2) Executa o código do módulo para criar objetos definidios no módulo;
3) Cria um namespace que residira os nomes desses objetos.''')

print("\n_____________________________________________________________________________")
#CLASSES
print('''\nNAMESPACES DE CLASSES - O mesmo vale para classes, o nome do namespace é o nome
da classe e dentro do namespace estão armazenado os nomes dos atributos das classes, 
como os métodos da classe.''')

print("\ndir(list)")
print(dir(list))

print("\nOUTRA FORMA DE CHAMAR OS MÉTODOS - Por isso podemos chamar os métodos de classes dessas forma:")

lista1 = [4, 8, 7, 6, 5, 9, 3, 1, 2, 10]
lista2 = [7, 6, 5, 9, 3, 1, 2, 10, 4, 8]
print("\nlista1 = [4, 8, 7, 6, 5, 9, 3, 1, 2, 10]")
print("lista2 = [7, 6, 5, 9, 3, 1, 2, 10, 4, 8]")
lista1.sort()
print('\nlista1.sort() -->', lista1)
list.sort(lista2)
print('list.sort(lista2) -->', lista2)

print("\n(As duas funcionam da mesma maneira)")
print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")