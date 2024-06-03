# Programa que solicita ao usuário que digite um número e em seguida informa o seu dobro, triplo e a raiz quadrada.

# Solicita ao usuário que digite um número.
num = int(input('Digite um número: '))

# Exibe o dobro, triplo e a raiz quadrada do número informado.
print(f'O dobro de {num} vale {num * 2}.\nO triplo de {num} vale {num * 3}\nA raiz quadrada de {num} é igual a {pow(num, 0.5):.2f}')
