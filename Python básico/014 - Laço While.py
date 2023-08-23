#LAÇO WHILE
print("_____________________________________________________________________________")
print('''\nLAÇO WHILE - Usado, principalmente, para repetições. Se a sua condição for verdadeira,
o bloco de código endentado pe executado, se não, ele pula pra instrução não edentada.''')

print("\nFORMATO DA INSTRUÇÃO WHILE:")
print('''\nwhile <condição>:
    <bloco de código endentado>
<instrução não endentada>''')


def pares(limite):
    lista_pares = []
    num = -2
    while num < limite:
        num = num + 2
        lista_pares.append(num)
    return lista_pares           

print("\nNúmeros pares: ", pares(10))

def ímpares(limite):
    lista_ímpares = [1]
    num = 1
    while num < limite:
        num = num + 2
        lista_ímpares.append(num)
    return lista_ímpares          

print("\nNúmeros ímpares: ", ímpares(10))

def fibbonaci(limite):
    lista_fibbonaci = [1, 1]  
    anterior = 1
    atual = 1
    while atual <= limite:
        anterior, atual = atual, atual+anterior
        lista_fibbonaci.append(atual)
    return lista_fibbonaci   

print("\nFibbonaci: ", fibbonaci(10))

print('\nOBS: Se quiser fazer um laço infinito, basta fazer "while True:".')

print("\n_____________________________________________________________________________")
print("\nBREAK - Interrompe a instrução de iteração mais próxima.")

print("\nNesse exemplo, com o BREAK, ele para de imprimir a linha da tabela quando encontra um 0:")
print("\ntabela = [[4, 0, 7], [2, 1, 0], [0, 0, 8]]")
tabela = [[4, 0, 7], [2, 1, 0], [0, 0, 8]]
def sem_zero(tabela): 
    for linha in tabela:
        for item in linha:
            if item == 0:
                break
            print(item, end = ' ')
        print()    
sem_zero(tabela)        

print('''\nPASS- Não faz nada (sem zoas). Usado nas raras ocasiões que você 
quer que um que um bloco de código não faça nada. Exemplo:''')

print('''\nn = 3
if n % 2 == 0:
    pass
else:
    print(n)''')

print('''\nCONTINUE - Continua a instrução inicia uma nova iteração da instrução de iteração mais próxima.''')

print("\nNesse exemplo, com o CONTINUE, ele só deixa de imprimir o 0 e não deixa de imprimir a linha:")
print("\ntabela = [[4, 0, 7], [2, 1, 0], [0, 0, 8]]")
tabela = [[4, 0, 7], [2, 1, 0], [0, 0, 8]]
def sem_zero(tabela): 
    for linha in tabela:
        for item in linha:
            if item == 0:
                continue
            print(item, end = ' ')
        print()    
sem_zero(tabela)        

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")