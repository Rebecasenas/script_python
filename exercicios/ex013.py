#Algoritmo que calcula um almento salarial com percentual de 15%

salarioStar = float(input('Qual é o salário do funcionário? R$'))
salarioEnd = salarioStar + ((salarioStar * 15) / 100)

print(f'Um funcionário que ganhava R${salarioStar}, com 15% de aumento, passa a receber R${salarioEnd:.2f}.')