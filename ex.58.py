#lista aleatória que separa os pares e os impares em duas novas listas
from random import randint

lista_principal= []
lista_pares= []
lista_impares= []
tamanho_lista= int(input('Tamanho lista: '))

for i in range(tamanho_lista):
    numeros= randint(0,100)
    lista_principal.append(numeros)
    if numeros %2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)





print(lista_principal)
print(lista_pares)
print(lista_impares)