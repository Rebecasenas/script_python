# Este programa sorteia nomes de uma lista para definir a ordem de apresentação.

# Importa o módulo random para realizar o sorteio
import random

# Lista de nomes dos alunos
nom_alun = ['Julia', 'Pedro', 'João', 'Mario']

# Sorteia 4 nomes distintos da lista de alunos
sorteio = random.sample(nom_alun, 4)

# Imprime a ordem de apresentação dos alunos sorteados
print(f'A ordem de apresentação será: {sorteio}')