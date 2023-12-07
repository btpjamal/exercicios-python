lista= []
pares=[]
for i in range(4):
    valores= int(input('digite um valor: '))
    lista.append(valores)
    if valores %2 == 0:
        pares.append(valores)

print(lista)
print(f'O número 9, apareceu {lista.count(9)} vezes na lista')

if 3 in lista:
    print(f'O número 3 apareceu pela primeira vez na posição {lista.index(3)}')
else:
    print('O número 3 não apareceu nenhuma vez na lista')

print(f'Os valores pares são: {pares}')



