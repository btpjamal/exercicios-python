#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

metros= int(input('unidade em metros: '))

centimetros= metros * 100
milimetros= metros * 1000

print(f'{metros} metros, resultou em {centimetros} cms, e em {milimetros} mms')