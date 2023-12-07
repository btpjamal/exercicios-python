lista= []
quantidade= int(input('quantidade de palavras: '))

for i in range(quantidade):
    palavras= str(input('palavra: '))
    lista.append(palavras)

for p in palavras:
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}')

