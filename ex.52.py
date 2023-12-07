#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero= int(input('Digite um número: '))
cont= 0
for i in range(1,numero + 1):
    if numero % i == 0:
        print(f'{i} é divisivel')
        cont+= 1
    else:
        print(f'{i} nao é divisivel')
print(f'O número {numero} foi dividido {cont} vezes')
if cont == 2:
    print(f'O Número {numero} é PRIMO')
else:
    print(f'Não é um número primo')
