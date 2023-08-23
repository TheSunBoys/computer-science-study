#PRINT, INPUT, EVAL
print("_____________________________________________________________________________")

print("\nprint() - Função que imprime na tela toda informação dada a ela, podendo ser uma string, operações ou váriaveis")
print("(Como eu estive fazendo aqui desde o início)")

print("\nx = 10")
print('print("x = 10")')
x=10
print(x)

print('\nprint("Bem vindo ao mundo do Python")')
print("Bem vindo ao mundo do Python")

print("\n_____________________________________________________________________________")

print("\ninput() - Função que exibe uma mensagem(ou não) e recebe um parâmetro do usuário.")

print('\nnome = input("Digite seu primeiro nome: )')
print("A variável 'nome' recebe uma STRING do usuário. Sim, o input() só recebe STRING")

x = input("\nDigite 5 para você ver: ")
print("x == 5 -->", x == 5)
print("x == '5' -->", x == '5')
print("( Se você quiser informar um valor que não seja uma string, você usa o eval() )")

print("\n_____________________________________________________________________________")

print("\neval() - Função que normalmente é colocada junto com o input() para avaliar o dado em uma não string")

print("\neval('3')")
print(eval('3'))

print("\neval('3 + 4')")
print(eval('3 + 4'))

print("\neval('len([1, 2, 3, 4]')")
print(eval('len([1, 2, 3, 4])'))

x = eval(input("\nDigite novamente 5 para você ver: "))
print("x == 5 -->", x == 5)
print("x == '5' -->", x == '5')

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")