from random import randint
valores= []
quantidade= int(input('quantidade: '))

for i in range(quantidade):
    numeros= randint(0,10)
    valores.append(numeros)

for posicao, valor in enumerate(valores):
    print(f'na posição {posicao}, temos o valor {valor}')
