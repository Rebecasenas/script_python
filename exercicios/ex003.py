# Este programa solicita ao usuário dois números inteiros, calcula a soma deles e imprime o resultado.

# Solicita ao usuário que insira o primeiro número e armazena o valor na variável 'n1'
n1 = int(input('Digite um número: '))

# Solicita ao usuário que insira o segundo número e armazena o valor na variável 'n2'
n2 = int(input('Digite mais um número: '))

# Calcula a soma dos dois números inseridos pelo usuário e armazena o resultado na variável 's'
s = n1 + n2

# Imprime a soma dos dois números inseridos pelo usuário
print('A soma vale {}'.format(s))
