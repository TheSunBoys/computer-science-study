#CLASSE TUPLE
print("_____________________________________________________________________________")

print('''\nTUPLAS - Tuplas são estruturas de dados permitem armazenar vários valores
relacionados em uma única variável. Elas são semelhantes às listas, mas são 
IMUTÁVEIS, o que significa que uma vez criada NÃO É POSSÍVEL...

- Adicionar elementos indivíduais da tupla 
- Remover elementos indivíduais da tupla 
- Alterar elementos indivíduais da tupla''')

print('''\nDIFERENTE DAS LISTAS, AS TUPLAS SÃO DELIMITADAS POR PARENTÊSES:

tupla = (1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]''')

tupla = (1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]

print("\nMANIPULAÇÃO DE TUPLAS:")
print("\nVerificando itens: tupla[1] --> ", tupla[1])
print("Modificando itens: tupla[1] = 7 --> ", TypeError)
print("Adicionando: tupla[5] = 6 --> ", TypeError)

print("\n_____________________________________________________________________________")
print("USOS DAS TUPLAS - Utilizando objetos tupla, podemos...")

print("\nRETORNAR MAIS DE UMA VALOR EM UMA FUNÇÃO:")

def soma_e_média(notas):
    soma = sum(notas)
    media = sum(notas)/3
    return (soma, media)
notas = [9.0, 8.0, 10.0]

print("Soma e média das notas = [8.0, 9.0, 7.5] -->", soma_e_média(notas))

print("\nUSAR UMA TUPLA COMO CHAVE DE UM DICIONÁRIO:")

empregado = {
    ('Albert, Wesker') : '050.181.570-98',
    ('Chris, Redfield') : '007.423.325-74',
    ('Jill, Valentine') : '049.242.407-65'
}

print("Passando tupla ('Albert, Wesker') como chave -->", empregado[('Albert, Wesker')])

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")