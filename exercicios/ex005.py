# Este programa solicita ao usuário que insira um número, em seguida, calcula e exibe o número antecessor e o número sucessor do número digitado. Cada parte do código está acompanhada de um comentário explicativo.

# Solicita ao usuário que digite um número.
num = int(input('Digite um número: '))

# Exibe o número informado pelo usuário, seu antecessor e seu sucessor.
print(f'Visto que o número informado foi {num}, o número antecessor é {num - 1} e o sucessor é {num + 1}.')