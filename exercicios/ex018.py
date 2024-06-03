# Este código Python solicita ao usuário que insira um ângulo em graus. Em seguida, ele calcula o seno, cosseno e tangente desse ângulo, convertendo-o para radianos antes de realizar os cálculos. Os valores resultantes são exibidos na tela com duas casas decimais. 
# Importa as funções sin, cos, tan e radians do módulo math.
from math import sin, cos, tan, radians

# Solicita ao usuário que digite o ângulo desejado.
ang = int(input('Digite o ângulo que você deseja: '))

# Calcula o seno, cosseno e tangente do ângulo fornecido, convertendo-o para radianos.
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

# Exibe o seno, cosseno e tangente do ângulo, formatando a saída com duas casas decimais.
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}.')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}.')
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}.')
