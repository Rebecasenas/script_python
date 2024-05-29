#Programa que lê um número real qualquer e mostra sua porção inteira.

#módulo importado
import math

#main------------
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.floor(num)}')