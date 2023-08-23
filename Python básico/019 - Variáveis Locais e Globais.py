#VARIÁVEIS LOCAIS E GLOBAIS
print("_____________________________________________________________________________")
print('''Variáveis LOCAIS - Declaradas dentro do escopo de um função.
Variáveis GLOBAIS - Declaradas fora do escopo de uma função''')

def dobro(y):
    x = 2 
    return y*x    
 
x = 0

print('''\ndef dobro(y):          
    x = 2                  #Todas as referências de x na função dobro são locais
    return y*x    
 
x = 0                      #Já aqui, temos uma variável global''')

print("\ndobro(3) =", dobro(3))
print("valor de x =", x)

print("\n(Com isso, vemos que as variáveis locais são visíveis apenas para o código dentro da função.)")

print("\n_____________________________________________________________________________")
print('''\nIMPORTANTE - Se uma variável for usada dentro de uma função, mas nenhum
valor é atribuído à ela, e essa mesma variável for declarada globalmente
com um valor, a função utilizará desse valor quando for trabalhar com a 
variável em questão.

EXEMPLO:''')

def multiplicar(y):
    return x*y

x = 0

print('''\ndef multiplicar(y):
    return x*y

x = 0''')

print('''\nValor de x = {0}
multiplicar(3) = {1}'''.format(x, multiplicar(3)))

print("\n(Aqui vemos que o x = 0 também foi usada na função multiplicar(), justamente por não ter sido declarado.")

print("_____________________________________________________________________________")
print("MUDANDO O VALOR DA VARIÁVEL GLOBAL - Se você quiser que a função mude o valor da variável global...")

def triplo(b):
    global a 
    a = 3 
    return b*a    
 
x = 0

print('''\ndef triplo(b):          
    global a 
    a = 3                 
    return b*a    
 
x = 0''')

print("\ntriplo(3) =", triplo(3))
print("valor de a =", a)

print("\n(Com isso, vemos que o valor de a foi MODIFICADO para 3.)")


print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")