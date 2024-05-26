#Algoritmo que lê  o preço de um produto e mostra seu novo preço, com 5% de desconto

precoStart = float(input('Qual é o preço do produto? R$'))
precoEnd = precoStart -  ((precoStart * 5) / 100)


print(f'O produto que custava R${precoStart:.2f}, na promoção com desconto de 5% vai custar R${precoEnd:.2f}')