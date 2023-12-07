# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_aleatorio = random.randint(0, 5)
chute_usuario = int(input('Chute um número de 0 a 5: '))

if chute_usuario == numero_aleatorio:
    print(f'O computador chutou: {numero_aleatorio}')
    print('Você venceu!!!')

else:
    print(f'O computador chutou: {numero_aleatorio}')
    print('Você Perdeu')