# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

alunos=[] # cria uma variavel de lista vazia
quant_alunos= int(input('quantidade de alunos: '))

for i in range(quant_alunos):  # usa a variavel criada como limite do range()

    nomes= input(f'digite o nome do aluno {i+1}: ')   # o {i+1} é o acumulador do range dentro do input
    alunos.append(nomes)  # append >>> adicionou o input da variavel "nomes" pra dentro da lista "alunos[]"

print(choice(alunos))       # escolheu alheatoriamente algo dentro da lista