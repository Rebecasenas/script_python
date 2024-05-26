#Programa que lê largura e altura de uma parede em metros, calcula sua área e quantidade de tinta necessária para pinta-la.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da prade: '))

#calculo metro quadrado
area = larg * alt

#a cada 2m² usamos 1L de tinta
tinta = area / 2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
