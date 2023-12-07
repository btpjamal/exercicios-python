#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços


frase=str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= junto[::-1] # fatiou o começo e o fim, -1 conta ao contrário
print(inverso)
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase não é um palíndromo')