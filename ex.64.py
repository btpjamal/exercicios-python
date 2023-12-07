#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
n= int(input('Número: '))
elemento1= 0
elemento2= 1
contador= 3
print(f'{elemento1} -> {elemento2} ', end='')
while contador <= n:
    elemento3= elemento1 + elemento2
    print(f'-> {elemento3} ', end='')
    elemento1= elemento2
    elemento2= elemento3
    contador+= 1
print('-> fim')
