# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


quantidade= 0
lista= []

while True:
    n= int(input('Digite um número: '))
    if n!= 999:
        lista.append(n)
        quantidade +=1
    else:
        break
print(f'fim do programa, foram digitados {quantidade} valores, e a soma entre eles é de {sum(lista)}')
