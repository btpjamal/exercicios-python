# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoas= []
quantidade= int(input('Informe a quantidade de pessoas: '))

for i in range(quantidade):
    peso= float(input('informe o peso: '))
    pessoas.append(peso)

print(f'Foram registrados os seguintes pesos: {pessoas}')
print(f'O maior peso é {max(pessoas)}, o menor é {min(pessoas)}')