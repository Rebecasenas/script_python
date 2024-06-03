# Este programa lê um número real qualquer, que o usuário informa através de um input e mostra a porção inteira do número.

# Importando o módulo necessário para utilizar a função trunc() que retorna a parte inteira de um número
from math import trunc

# Função principal
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e seua porção inteira é {trunc(num)}')

# Alternativamente, para este exercício, poderíamos usar a função int() diretamente sem importar o módulo math.