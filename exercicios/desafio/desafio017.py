# Programa para calcular comprimento do cateto oposto e o adjacente de um triangulo retangulo, calcular e mostre o comprimento da hipotenusa.

#módulo math importado para usar função pow e sqrt no Teorema de Pitágoras
import math

# main-----------

# Solicitar os valores dos catetos ao usuário
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))

# Calcular a hipotenusa usando o Teorema de Pitágoras
h = math.sqrt((pow(co, 2)) + (pow(ca, 2)))

# Exibir o resultado com duas casas decimais
print(f'O cumprimento da hipotenusa é {h:.2f}')