#EXCEPT E TRY
print("_____________________________________________________________________________")

print('''\nTRY E EXCEPT - O try e except são estruturas de controle de fluxo em Python
que permitem lidar com exceções, ou seja, situações em que um erro pode ocor-
rer durante a execução do programa.''')

print('''\nEXEMPLO DO MODELO DE USO:

try:
    <bloco de código endentado 1>
except:
    <bloco de código endentado 2>
<bloco de código não ententado>

AQUI UM EXEMPLO DE CÓDIGO COM TRY E EXCEPT:

def sua_idade():
    try:
        idade_str = input("Digite sua idade: ")
        idade_int = int(idade_str)
        print("Você tem { 0 } anos".format(idade_int))
    except:
        print("Digite uma idade com números!")
''')

def sua_idade():
    try:
        idade_str = input("Digite sua idade: ")
        idade_int = int(idade_str)
        print("Você tem {0} anos".format(idade_int))
    except:
        print("Digite uma idade com números!")

print("\nExperimente digitar um número inteiro: ")
print()
sua_idade()
print()
print("\nAgora, digite um texto (tipo 'quinze'): ")
print()
sua_idade()
print()

print("\n_____________________________________________________________________________")

print('''\nMANIPULADORES DE EXCEÇÕES - Pode existir quantos excepts nós quisermos e ainda
podemos indicar o tipo de erro em cada um:''')

print('''def sua_idade2():
    try:
        idade_str = input("Digite sua idade: ")
        idade_int = int(idade_str)
        print("Você tem { 0 } anos".format(idade_int))
    except IOError:
        print("Erro de entrada/saída")
    except ValueError:
        print("Valor não pode ser convertido para inteiro")
    except:
        print("Algum outro erro aconteceu.")
        
(Ou seja, se identicar o erro como IOError, uma mensagem aparece, se identificar como
ValueError, outra mensagem aparece, se não for nenhum dos dois, a mensagem final aparece)''')        

print("\n_____________________________________________________________________________")
print("IDENTIFICANDO ERROS")

funcao = '''\ndef h(n):
    print("Funçao h")
        print(1/n)
    except:
        print("Erro encontrado!")

def g(n):
    print("Funçao g")
    h(n-1)
    print(n)

def f(n):
    print("Funçao f")
    g(n-1)
    print(n)'''        

print(funcao)
print('''\nNa função f, chega um momento que, após chamar a função f, acontece uma 
divisão por zero quando f(2). Com isso podemos usar try e except pra quando isso ocorrer.''')

funcao2 ='''\ndef h(n):
    print("Funçao h")
    try:
        print(1/n)
        print(n)
    except:
        print("Erro encontrado!")

def g(n):
    print("Funçao g")
    h(n-1)
    print(n)

def f(n):
    print("Funçao f")
    g(n-1)
    print(n)'''

print(funcao2)

def h(n):
    print("Funçao h")
    try:
        print(1/n)
        print(n)
    except:
        print("Erro encontrado!")

def g(n):
    print("Funçao g")
    h(n-1)
    print(n)

def f(n):
    print("Funçao f")
    g(n-1)
    print(n)
print()
f(2)  

print("\n_____________________________________________________________________________")

print("\nAQUI TEM UMA LISTA DE ERROS PRA CASO QUEIRA USAR:")

lista_de_erros = '''\nSyntaxError: ocorre quando a sintaxe do código não está correta.

IndentationError: ocorre quando a indentação do código não está correta.

NameError: ocorre quando uma variável ou função é referenciada antes de ser definida.

TypeError: ocorre quando se tenta fazer uma operação com tipos de dados incompatíveis.

ValueError: ocorre quando o tipo de dado é correto, mas o valor não é adequado.

KeyError: ocorre quando se tenta acessar uma chave que não existe em um dicionário.

IndexError: ocorre quando se tenta acessar um índice que está fora do limite de uma lista ou tupla.

AttributeError: ocorre quando se tenta acessar um atributo que não existe em um objeto.

ImportError: ocorre quando um módulo não pode ser importado.

OSError: ocorre quando ocorre um erro de sistema, como permissão negada ou arquivo não encontrado.'''

print(lista_de_erros)

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")