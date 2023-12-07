#Um programa para criar uma lista aleatória de tamanho definido pelo usuário
from random import randint

lista= []
tamanho_lista= int(input('tamanho lista: '))

for i in range(tamanho_lista):
    numeros= randint(0,10)
    lista.append(numeros)


print(lista)