#STRINGS

import math
import fractions

print("_____________________________________________________________________________")
print("\nMÓDULO math - Biblioteca de constantes e funções matemáticas")

print("\nmath.sqrt(x) - Calcula a raiz quadrada de x")
print("math.sqrt(49) =", math.sqrt(49))

print("\nmath.ceil(x) - Menor inteiro que é >= x")
print("math.ceil(2.31) =", math.ceil(2.31))

print("\nmath.floor(x) - Maior inteiro que é <= x")
print("math.floor(2.31) =", math.floor(2.31))

print("\nmath.cos(x) - Cosseno de x")
print("math.cos(0) =", math.cos(0))

print("\nmath.sin(x) - Seno de x")
print("math.sin(0) =", math.sin(0))

print("\nmath.log(x, base) - Log de x na base")
print("math.log(32, 2) =", math.log(32, 2))

print("\nmath.pi - Valor de pi")
print(math.pi)

print("\nmath.e - Constante de Euler")
print(math.e)

print("\n_____________________________________________________________________________")
print("\nMÓDULO fractions - Usado para representar frações e realizar aritmética racional")

a = fractions.Fraction(3, 4)
print("\na = fractions.Fraction(3, 4) -->", a)

b = fractions.Fraction(1, 2)
print("\nb = fractions.Fraction(1, 2) -->", b)

print("\na + b =", a + b)
print("\na * b =", a * b)

print("\n_____________________________________________________________________________")
print("\nBÔNUS: CONVERSÃO DE VARIÁVEIS")

print("\nx = 4.5")
x = 4.5
print("int(x) =", int(x))

print("\ny = 3")
y = 3
print("float(y) =", float(y))

print("\n_____________________________________________________________________________")
input("\nPressione qualquer tecla para fechar...")