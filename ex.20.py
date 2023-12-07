# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle # shuffle = embaralhar
alunos= []
quant_alunos= int(input('quantidade de alunos: '))

for i in range(quant_alunos):
    nomes=(input(f'nome do aluno {i+1}: '))
    alunos.append(nomes)
    shuffle(alunos)


print(alunos)