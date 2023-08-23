#LISTAS BIDIMENSIONAIS
print("_____________________________________________________________________________")
print("\nLISTAS BIDIMENSIONAIS - É possível fazer listas bidimensionais no Python a partir do seguinte formato:")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

texto = '''\nmatriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] onde...
matriz[linha][coluna]'''
print(texto)

print("\nIMPRIMINDO A MATRIZ:")
def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
imprimir_matriz(matriz)        

print("\nIMPRIMINDO OS ITENS DA MATRIZ:")
def imprimir_itens(matriz):
    for linha in matriz:
        for item in linha:
            print(item, end=' ')
        print()  
imprimir_itens(matriz)          

print("\nSOMANDO DUAS MATRIZES:") 

matrizes = '''matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
matriz2 = [[4, 3, 2], [1, 0, -1], [-2, -3, -4]]  
'''
print(matrizes)

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   
matriz2 = [[4, 3, 2], [1, 0, -1], [-2, -3, -4]] 
matriz3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def soma(matriz1, matriz2, matriz3):
    for i in range(3):
        for j in range(3):
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

soma(matriz1, matriz2, matriz3)
imprimir_matriz(matriz3)


print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")