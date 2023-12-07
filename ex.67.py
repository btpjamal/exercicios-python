#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n= int(input('Digite um número: '))
    tabuada = 0
    if n >= 0:
        for i in range(11):
            print(f'{n} * {tabuada} = {n* tabuada}')
            tabuada+= 1
    elif n < 0:
        break
print('Fim do programa')


    
