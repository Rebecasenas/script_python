# Este programa solicita ao usuário dois números, realiza a soma e exibe o resultado.

# Solicita ao usuário que insira o primeiro número e armazena o valor na variável 'a'
a = int(input('Qual o primeiro número? '))

# Solicita ao usuário que insira o segundo número e armazena o valor na variável 'b'
b = int(input('Qual o segundo número? '))

# Calcula a soma dos dois números inseridos pelo usuário e armazena o resultado na variável 'c'
c = a + b

# Imprime a soma dos dois números inseridos pelo usuário
print('A soma de {} mais {} é {}'.format(a, b, c))