#FUNÇÕES
print("_____________________________________________________________________________")

print("\nDEF - Utilizado para definir funções, aqui um exemplo de como usá-lo:")

print("\ndef função(x):")
print("     return x + 5")

print("\nSe você quiser invocá-la para qualquer valor, é só usar função(5)")

print("\n_____________________________________________________________________________")
print("\nExemplo de função que calcula o quadrado de uma valor")

print("\ndef quadrado(x):")
print("     return x**2")

def quadrado(x):
    return x**2

print("\nPassando 2 como parâmetro: ", quadrado(2))
print("Passando 3 como parâmetro: ", quadrado(3))
print("Passando 4 como parâmetro: ", quadrado(4))
print("Passando 5 como parâmetro: ", quadrado(5))

print("\n_____________________________________________________________________________")
print("\nRETURN VS PRINT")

print("\nreturn - Irá retornar o valor resultante como uma NÃO STRING sem imprimí-lo na tela")

print("\nprint - Irá retornar o valor resultante como uma STRING imprimindo-o na tela")

print("(Se quiser usar um ou outro vai depender do caso)")

print("\n_____________________________________________________________________________")

print("\nDOCSTRINGS - Basicamente, você pode colocar uma string dentro de uma função para especificar o que aquela esse função faz. Como coloque na função abaixo (veja abrindo por um editor):")

def cubo(x):
    'Função que calcula o cubo de um número'
    return x**3

print("\nQuando você quiser consultar esse docstring, é só utilizar help(nome da função)\n")
help(cubo)


print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")