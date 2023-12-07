from random import randint
lista= []
tamanho_lista= int(input('tamanho lista: '))
for i in range(tamanho_lista):
    numeros= randint(1,10)
    if numeros not in lista:
            lista.append(numeros)


print(lista)
print(max(lista))
print(min(lista))