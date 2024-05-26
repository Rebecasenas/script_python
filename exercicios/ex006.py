#programa que informa o dobro, triplo e a raiz quadrada do valor informado

#main-----
num = int(input('Digite um número: '))

print(f'O dobro de {num} vale {num * 2}.\nO triplo de {num} vale {num * 3}\nA raiz quadrada de {num} é igual a {pow(num, 0.5):.2f}')