# Programa quie lê um ângulo qualquer e mostra na tela o valor do senho, cosseno e tangente desse ângulo

# modulo math importado 
from math import sin, cos, tan, radians

ang = int(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'O ângulo de {ang} tem o SENO de {seno:.2f}.')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}.')
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}.')