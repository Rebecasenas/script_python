# Sorteio de números. Sortear um aluno usando seu número na chamada

# Modulo random importado para randomizar números
import random

# Lista dos alunos na fila para a tarefa, juntamente com seus números na chamada
print('Alunos na fila para a tarefa:\nAline/1, Junior/2, Marcos/3, Sonia/4')

# Sorteia um número inteiro e aleatório entre 1 e 4 para representar o aluno escolhido
aluno = random.randint(1, 4)

# Imprime o número do aluno escolhido
print(f'O aluno escolhido foi: {aluno}')