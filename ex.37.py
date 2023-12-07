# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num= int(input('Número: '))
print('''Selecione a base numérica:
[1] para binário
[2] para octal
[3] para hexadecimal''')
select= int(input())

if select == 1:
    print(bin(num))
elif select == 2:
    print(oct(num))
elif select ==3:
    print(hex(num))
else:
    print('Número inválido')