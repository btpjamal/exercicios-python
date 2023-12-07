#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n= int(input('Digite um número: '))
c= 0
while n!= 999:
    soma= n + c
    if c != 999:
        n= int(input('Digite mais um número: '))
        c+=1
print(f'fim, você digitou {c} números, a soma entre eles é {soma}')