# Este programa calcula a hipotenusa de um triângulo retângulo, dado o comprimento do cateto oposto e do cateto adjacente. Ele solicita ao usuário que insira o comprimento desses dois catetos, usa a fórmula do Teorema de Pitágoras para calcular a hipotenusa e, em seguida, imprime o resultado formatado com duas casas decimais.

# Importando as funções sqrt (raiz quadrada) e pow (potência) do módulo math.
from math import sqrt, pow

# Solicitando ao usuário o comprimento do cateto oposto e do cateto adjacente.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# Calculando a hipotenusa usando o Teorema de Pitágoras e atribuindo o resultado à variável h.
h = sqrt((pow(co, 2)) + (pow(ca, 2)))

# Exibindo o resultado formatado com duas casas decimais.
print(f'A hipotenusa vai medir {h:.2f}')

## Outra forma mais simples seria importar a função hypot() do módulo math para calcula a hipotenusa de um triângulo retângulo.
## h = hypot(ca, co)
