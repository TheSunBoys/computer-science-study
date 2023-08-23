#DATA E HORA
print("_____________________________________________________________________________")

import time
print("\nMÓDULO TIME - Modulo que fornece várias funções relacionadas a tempo.")

print("\ntime.localtime() - Fornece o horário atual.")
print(time.localtime())

print("\ntime.strftime() - Fornece o horário no formato desejado.")
print('time.strftime("diretiva", time.localtime())')

print("\nLista de diretivas: ")

lista = '''%A - Dia da semana completo.
%a - Dia da semana abreviado.
%B - Nome do mês completo.
%b - Nome do mês abreviado.
%d - Dia do mês.
%H - Horas (00 e 23).
%I - Horas (1 e 12).
%M - Minutos.
%p - AM ou PM.
%S - Segundos.
%y - Ano (0 e 99).
%Y - Ano (número de 4 digitos).
%Z - Nome do fuso horário. '''

print(lista)

print("\n_____________________________________________________________________________")

data = time.strftime("%A, %d de %B de %Y", time.localtime())
horario = time.strftime("%H:%m:%S", time.localtime())

print("DATA: ", data, "\nHORÁRIO: ", horario)

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")
