# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1= int(input('Número 1: '))
num2= int(input('Número 2: '))
num3= int(input('Número 3: '))
lista= []

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'''o menor é: {min(lista)}
e o maior é: {max(lista)}''')