#MÉTODOS DE STRINGS
print("_____________________________________________________________________________")
print("\nASPAS TRIPLAS (''' ''') - São usadas para definir uma string de várias linhas,")

jogos = '''
dark souls é um jogo de fantasia medieval.
bloodborne é um jogo de horror cósmico e temática gótica.
sekiro é um jogo que se passa em um cenário de japão feudal.
'''

print("\nComo exemplo, veja o texto que atribui à variável jogos: ")
print(jogos)

print("\n_____________________________________________________________________________")
print("\nMÉTODOS USADOS EM STRINGS:")

print('\ns = "palavra"') 
s = "palavra"

print("\ns.captitalize() - Cópia da string com primeiro caractere com letra maiúscula (NÃO MODIFICA).")
print(s.capitalize())

print('\njogos.count("jogo") - Número de vezes que a substring "jogo" aparece no texto jogos.')
print(jogos.count('jogo'))

print("\ns.lower() - Cópia da string com os caracteres em minúsculo (NÃO MODIFICA).")
print(s.lower())

print("\ns.upper() - Cópia da string com os caracteres em minúsculo (NÃO MODIFICA).")
print(s.upper())

print("\njogos.replace('jogo', 'game') - Substitui todas as ocorrências de uma substring por outra (NÃO MODIFICA).")
print("(Nesse caso, substitui 'jogo' por 'game')")
print(jogos.replace('jogo', 'game'))

print("\njogos.find('jogo') - Índice da primeira ocorrência da substring 'jogo' na string jogos.")
print(jogos.find('jogo'))

print('\nfrase = "Batata cozida é muito bom"')
frase = "Batata cozida é muito bom"

print("\nfrase.split() - Uma lista de substrings da string frase usando o delimitador ',' por padrão.")
print(frase.split())

print("\nstr.makestrans e frase.translate(tabela) - Apenas veja a funcionalidade: ")

print("\ntabela = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyzabc')")
tabela = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyzabc')
print("\nfrase.translate(tabela) --->",frase.translate(tabela))

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")