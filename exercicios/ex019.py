# Em resumo, o programa seleciona aleatoriamente um dos alunos inseridos pelo usuário e o exibe como o aluno escolhido.

# Importando a função choice do módulo random
from random import choice  

# Criando uma lista vazia para armazenar os alunos
lista_alunos = []

# Adicionando alunos à lista utilizando input para receber os nomes
lista_alunos.append(input('Primeiro aluno: '))  # Recebe o nome do primeiro aluno
lista_alunos.append(input('Segundo aluno: '))   # Recebe o nome do segundo aluno
lista_alunos.append(input('Terceiro aluno: '))  # Recebe o nome do terceiro aluno
lista_alunos.append(input('Quarto aluno: '))    # Recebe o nome do quarto aluno

# Escolhendo aleatoriamente um aluno da lista
busca_aluno = choice(lista_alunos)

# Imprimindo o nome do aluno escolhido aleatoriamente
print(f'O aluno escolhido foi {busca_aluno}')
