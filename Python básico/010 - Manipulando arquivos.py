#MANIPULANDO ARQUIVOS
print("_____________________________________________________________________________")

print("\nMANIPULAÇÃO DE ARQUIVOS")

print('\narquivo = open("caminho", "modo")')

print('\nNo meu caso, o CAMINHO é "/010 - Manipulando arquivos/texto-leitura.txt"')

modos = '''r - modo de leitura (padrão)
w - modo de gravação (se o arquivo já existir, seu conteúdo é apagado)
a - modo de acréscimo (o conteúdo é acrescentado ao final do arquivo)
r+ - modo de leitura e gravação 
t - modo de texto (padrão)
b - modo binário'''

print("\nEm relação aos MODOS, temos o seguintes:\n")
print(modos)

print("\n_____________________________________________________________________________")
print("\nLEITURA DE ARQUIVOS")

print("\nABRINDO O ARQUIVO (Lembre-se de criar uma variável):")
print('arquivo = open("/010 - Manipulando arquivos/lista-leitura.txt", "r")')

arquivo = open("/010 - Manipulando arquivos/texto-leitura.txt", "r")
print("\nVERIFICAR SE É POSSÍVEL LER ARQUIVO:")
print("arquivo.readable() -->", arquivo.readable())
arquivo.close()

arquivo = open("/010 - Manipulando arquivos/texto-leitura.txt", "r")
print("\narquivo.read() - Lê arquivo até o final e retorna como uma string")
print(arquivo.read())
arquivo.close()

arquivo = open("/010 - Manipulando arquivos/texto-leitura.txt", "r")
print("\narquivo.readline() - Lê arquivo de linha em linha e retorna a linha correspondente como uma string")
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
arquivo.close()

arquivo = open("/010 - Manipulando arquivos/texto-leitura.txt", "r")
print("\narquivo.readlines() - Lê arquivo até o final e retorna uma lista de linhas como uma string")
print(arquivo.readlines())
arquivo.close()

print("\nFECHANDO ARQUIVO:")
print("arquivo.close()")

obs = '''OBS: Você deve está se perguntando porque está cheio de "arquivo = open(...)" e
"arquivo.close()" no código, digamos que só é possível fazer essa leitura uma 
vez, por isso que repeti inúmeras vezes essas linhas no código. Com meu
conhecimento atual, foi isso que entendi, posso estar errado.'''
print("\n", obs)

print("\n_____________________________________________________________________________")
print("\nGRAVAÇÃO EM ARQUIVOS")

arquivo = open("/010 - Manipulando arquivos/texto-gravação.txt", "a")

print('arquivo.write("Elden Ring") - Acabei de adicionar "Elden Ring" no arquivo com esse comando')

arquivo.write("\nElden Ring")
arquivo.close()

print("\nOBS: Também posso usar o modo 'w' pra fazer isso, mas esse processo apagaria tudo de meu arquivo")

print("\n_____________________________________________________________________________")
print("\nOBS: Escrevi outros textos no código, recomendo ler eles também")
print("\n_____________________________________________________________________________")

# print("\n_____________________________________________________________________________")
# print("\nCRIANDO NOVO ARQUIVO")

# arquivo = open("/010 - Manipulando arquivos/texto3.txt", "x")

# print('arquivo.write("\nDark Souls I\nDark Souls II\nDark SoulsIII") - Criei um novo arquivo e adicionei esses itens com esse comando')
# arquivo.write("\nDark Souls I\nDark Souls II\nDark Souls III")

# arquivo.close()

# print("\n_____________________________________________________________________________")
# print("REMOVENDO ARQUIVOS")

# import os
# os.remove("Estudo de Python/texto3.txt")

input("\nPressione qualquer tecla para fechar...")

