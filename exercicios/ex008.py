#Programa que converte distâncias em metros para diferentes medidas de distância.

#main
distancia = float(input('Uma distância em metros: '))
print(f'A medida de {distancia} corresponde a:')

#Formulas
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

#Impressão de dados
print(f'{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')



