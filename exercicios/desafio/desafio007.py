# Solicita ao usuário que insira sua nota em matemática e armazena o valor como um número inteiro
a = int(input('Qual sua nota em matemática? '))

# Solicita ao usuário que insira sua nota em programação e armazena o valor como um número inteiro
b = int(input('Qual sua nota em progamação? '))

# Calcula a média das duas notas inseridas pelo usuário e armazena o valor como um número de ponto flutuante
m = float((a + b) / 2)

# Imprime a média calculada usando formatação de string e substituindo {} pelo valor de m
print('Sua média é: {}'.format(m))