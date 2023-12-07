#O computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cpu = randint(0,10)
player= int(input('Tente adivinhar o número de 0 a 10: '))
contador_tentativas=1

while player != cpu:
    contador_tentativas+= 1
    if cpu > player:
        print('Mais... tente novamente')
    elif cpu < player:
        print('Menos... tente novamente')
    player= int(input('Um número de 0 a 10: '))
print(f'Você acertou com {contador_tentativas} tentativas')
