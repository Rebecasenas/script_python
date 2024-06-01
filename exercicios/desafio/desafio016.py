# Programa que lê um número real qualquer e mostra sua porção inteira.

# Módulo importado para usar a função de arredondamento para baixo (floor)
import math

# Função principal
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.floor(num)}')