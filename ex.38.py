# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1= int(input('Número 1: '))
num2= int(input('Número 2: '))

if num1 > num2:
    print('O primeiro Valor é maior')
elif num2 > num1:
    print('O segundo Valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')