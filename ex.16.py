#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc    #floor arredonda pra baixo, ceil arredonda pra cima, trunc pega o numero antes da virgula
n= float(input('Número: '))
arredondar= trunc(n)      # int(n) >>> tbm funcionaria

print(f'''O numero digitado foi: {n}
o arredondamento é: {arredondar}''')
