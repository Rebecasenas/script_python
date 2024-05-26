#Algoritmo que calcula o valor do aluguel de um carro. Levando em consideração que a diaria custa R$60 e R$0,15 por Km rodado.

dia = int(input('Quantos dia alugados? '))
km = int(input('Quantos Km rodados? '))
total = (60 * dia) + (0.15 * km)

print(f'O total a pagar é de R${total:.2f}')