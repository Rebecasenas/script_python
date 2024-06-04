# Este programa cria uma lista vazia para armazenar os nomes de quatro alunos, solicita que o usuário insira os nomes desses alunos e, em seguida, embaralha aleatoriamente os nomes usando a função `sample()` do módulo `random`. Em seguida, imprime a ordem aleatória dos nomes dos alunos. Este commit adiciona comentários ao código para melhorar sua legibilidade e compreensão.

# Importando as funções sample do módulo random
from random import sample  

# Criando uma lista vazia para armazenar os alunos
lista = []

# Adicionando alunos à lista utilizando input para receber os nomes
lista.append(input('Aluno 1: '))  # Recebe o nome do primeiro aluno
lista.append(input('Aluno 2: '))  # Recebe o nome do segundo aluno
lista.append(input('Aluno 3: '))  # Recebe o nome do terceiro aluno
lista.append(input('Aluno 4: '))  # Recebe o nome do quarto aluno

# Embaralhando aleatoriamente a lista de alunos
sorteio = sample(lista, 4)  

# Imprimindo a ordem de sorteio dos alunos
print(f'A ordem do sorteio foi {sorteio}')
