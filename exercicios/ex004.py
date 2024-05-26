#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

j = input('Digite o que quiser: ')
print('O tipo primitivo desse valor é: ', type(j))
print('Só tem espaço ? ', j.isspace())
print('É um número? ', j.isnumeric())
print('É alfabeto? ', j.isalpha())
print('É alfanumerico? ', j.isalnum())
print('Está em maiúscula? ', j.isupper())
print('Está em minúscula? ', j.islower())
