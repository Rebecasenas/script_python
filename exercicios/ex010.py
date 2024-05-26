#Programa que converte real em outras moedas, considere:
#US$1,00 = R$5,14 -- EUR1,00 = R$5,55 -- GBP£1,00 = R$6,52(cotação em 23/05/24)

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.14 
eur = real / 5.55
gbp = real / 6.52

print(f'Com {real:.2F} você pode comprar US$ {dolar:.2f}, EUR€ {eur:.2f} ou GBP£ {gbp:.2f}')