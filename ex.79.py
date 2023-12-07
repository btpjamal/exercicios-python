lista= []
quantidade= int(input('quantidade: '))

for i in range(quantidade):
    valores= int(input(f'valor {i}: '))
    while True:
        if valores not in lista:
            lista.append(valores)
            break
        else:
            print('valor já digitado, tente novamente...')
            valores= int(input(f'valor {i}: '))
            continue

print(f'Os valores únicos em ordem crescente: {sorted(lista)}')
         