#Criar um programa para jogar jokenpo
import random
from random import randint

itens= ('Pedra', 'Papel', 'Tesoura')
computador= random.randint(0,2)
jogador= int(input('''Faça a sua jogada!!!
[0]- Pedra
[1]- Papel
[2]- Tesoura

:'''))

print('-=' * 20)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu: {itens[computador]}')
print('-=' * 20)

if computador == 0:  # computador escolheu   PEDRA
    if jogador == 0: # jogador   escolheu    PEDRA
        print('EMPATOU')

    elif jogador == 1: # jogador escolheu PAPEL
        print('JOGADOR GANHOU')

    elif jogador == 2: # jogador escolheu TESOURA
        print('COMPUTADOR GANHOU')

elif computador == 1: # computador escolheu PAPEL
    if jogador == 0:  # jogador escolheu PEDRA
        print('COMPUTADOR GANHOU')

    elif jogador == 1: # jogador escolheu PAPEL
        print('EMPATOU')

    elif jogador == 2: # jogador escolheu TESOURA
        print('JOGADOR GANHOU')

elif computador == 2: # computador escolheu TESOURA
    if jogador == 0: # jogador escolheu PEDRA
        print('JOGADOR GANHOU')

    elif jogador == 1: # jogador escolheu PAPEL
        print('COMPUTADOR GANHOU')

    elif jogador == 2: # jogador escolheu TESOURA
        print('EMPATOU')