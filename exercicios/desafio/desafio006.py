# Solicita ao usuário que insira um número e armazena o valor como um número inteiro
a = int(input('Digite um número: '))

# Calcula o dobro do número inserido pelo usuário e armazena o valor como um número inteiro
dobro = int(a * 2)

# Calcula o triplo do número inserido pelo usuário e armazena o valor como um número inteiro
triplo = int(a * 3)

# Calcula a raiz quadrada do número inserido pelo usuário e armazena o valor como um número inteiro
raiz = int(a ** 1/2)

# Imprime o dobro, triplo e a raiz quadrada do número inserido pelo usuário usando formatação de string
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}.'.format(a, dobro, triplo, raiz))