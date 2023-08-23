#DICIONÁRIOS
print("\_____________________________________________________________________________")
print('''\nDICIONÁRIO - Às vezes, utilizar listas em Python não é funcional, por isso que essa
lingauagem possuí uma contêiner imbutido chamado dicionário, onde podemos atribuir
valores à chaves fornecidas pelo usuário.''')

texto1 = '''\nempregado = {
'050.181.570-98' : ['Albert Wesker'],
'007.423.325-74' : ['Chris Redfield'],
'049.242.407-65' : ['Jill Valentine']
}'''

print(texto1)

empregado = {
'050.181.570-98' : ['Albert Wesker'],
'007.423.325-74' : ['Chris Redfield'],
'049.242.407-65' : ['Jill Valentine']
}

print("\nempregado['007.423.325-74'] --> ", empregado['007.423.325-74'])
print("empregado['049.242.407-65'] -->", empregado['049.242.407-65'])
print("empregado['050.181.570-98'] -->", empregado['050.181.570-98'])

print("\n_____________________________________________________________________________")

print("PROPRIEDADES DA CLASSE DICIONÁRIO - Também podemos fazer o mesmo nesse seguinte formato...")

print("\nvariável = {<chave 1>:<valor 1>, <chave 2> : <valor 2>, ..., <chave i> : <valor i>}")

print("\ndias = {'seg':'segunda-feira', 'ter':'terça-feira', 'qua':'quarta-feira', 'qui':'quinta-feira', 'sex':'sexta-feira'}")

dias = {'seg':'segunda-feira', 'ter':'terça-feira', 'qua':'quarta-feira', 'qui':'quinta-feira', 'sex':'sexta-feira'}

print("\ndias['seg'] --> {0}\ndias['ter'] --> {1}\ndias['qua'] --> {2}\ndias['qui'] --> {3}\ndias['seg'] --> {4}".format(dias['seg'], dias['ter'], dias['qua'], dias['qui'], dias['sex']))

print('\nTAMBÉM É POSSÍVEL MODIFICAR OU ADICIONAR NOVOS VALORES')

print('''\ndias['sáb'] = 'sábado'
dias['sex'] = 'SEXTA-FEIRA''')

dias['sáb'] = 'sábado'
dias['sex'] = 'SEXTA-FEIRA'
print()
print(dias)

print("\n_____________________________________________________________________________")
print('\nMÉTODOS DE DICIONÁRIO')

print('\ndias.items() - ', dias.items())

print('\ndias.keys() - ', dias.keys())

print('\ndias.values() - ', dias.values())

print("\nd.get(chave) - dias.get('qua') -->", dias.get('qua'))

dias.pop('sáb')
print("\nd.pop(chave) - dias.pop('sáb') -->", dias)

print("\nfds = {'sab':'sábado', 'dom' : 'domingo'}")
fds = {'sab':'sábado', 'dom' : 'domingo'}
print("\ndias.update(fds)")
dias.update(fds)
print("\ndias =", dias)

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")