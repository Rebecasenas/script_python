n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))

s = n1 + n2

#forma antiga de fazer string adicionando variaveis: print(' some de', n1, 'mais', n2, 'é igual a', s)

print('a soma entre {} e {} vale {}' .format(n1, n2, s))