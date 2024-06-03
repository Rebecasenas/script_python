# Programa que lê algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Solicita ao usuário que digite algo pelo teclado.
j = input('Digite o que quiser: ')

# Exibe o tipo primitivo do valor digitado.
print('O tipo primitivo desse valor é: ', type(j))

# Verifica se o valor contém apenas espaços em branco e exibe o resultado.
print('Só tem espaço ? ', j.isspace())

# Verifica se o valor é numérico e exibe o resultado.
print('É um número? ', j.isnumeric())

# Verifica se o valor é composto apenas de caracteres alfabéticos e exibe o resultado.
print('É alfabeto? ', j.isalpha())

# Verifica se o valor é composto apenas de caracteres alfanuméricos e exibe o resultado.
print('É alfanumérico? ', j.isalnum())

# Verifica se todas as letras do valor estão em maiúsculas e exibe o resultado.
print('Está em maiúscula? ', j.isupper())

# Verifica se todas as letras do valor estão em minúsculas e exibe o resultado.
print('Está em minúscula? ', j.islower())
