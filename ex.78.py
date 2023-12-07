lista= []

for i in range(5):
    numeros= int(input(f'numero {i}: '))
    lista.append(numeros)

print(f'O maior número é: {max(lista)} na posição: {lista.index(max(lista))}')
print(f'O menor número é: {min(lista)} na posição: {lista.index(min(lista))}')
