# Este programa solicita ao usuário um número inteiro e exibe seu antecessor e sucessor.

# Solicita ao usuário que insira um número inteiro e armazena o valor na variável 'a'
a = int(input('Digite um número: '))

# Calcula o antecessor do número inserido pelo usuário subtraindo 1 de 'a' e armazena o resultado na variável 'b'
b = int(a - 1)

# Calcula o sucessor do número inserido pelo usuário somando 1 a 'a' e armazena o resultado na variável 'c'
c = int(a + 1)

# Imprime o antecessor e o sucessor do número inserido pelo usuário
print('O antecessor é {} e o sucessor é {}'.format(b, c))