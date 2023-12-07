#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint


vitorias= 0
while True:
    par_impar= str(input('Ecolha par ou ímpar: '))
    jogador= int(input('Jogue um número (0 a 10): '))
    cpu= randint(0, 10)
    print(f'A CPU jogou {cpu}')
    soma = cpu + jogador
    if jogador %2== 0 and cpu%2==0 or jogador %2!= 0 and cpu %2!=0:
        print('Ambos pensaram em números que resultariam em empate')
        continue
    if cpu %2==0:
        print('CPU escolheu par')
    else:
        print('CPU escolheu ímpar')
    print(soma)
    if soma %2==0:
        if 'par' in par_impar.lower():
            print('jogador ganhou')
            vitorias += 1       
        elif 'impar' in  par_impar.lower():
            print('cpu ganhou')
            break
    else:
        if 'impar' in par_impar.lower():
            print('jogador ganhou')
            vitorias+=1
        elif 'par' in par_impar.lower():
            print('CPU ganhou')
            break
print(f'Fim de jogo, com {vitorias} vitorias')











