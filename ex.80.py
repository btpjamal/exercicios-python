#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n= int(input('Digite um valor: '))
quantidade= 0
lista= []
lista.append(n)
parar= False
while parar == False:
    resposta= str(input('Deseja digitar mais algum valor? (s/n): '))
    if resposta.lower() == 's':
        n= int(input('Digite mais um valor: '))
        lista.append(n)
        quantidade +=1
    elif resposta.lower() == 'n':
        parar = True
        media = n / quantidade
print(f'fim do programa, a media dos valores é {media}, o maior valor digitado foi {max(lista)} e o menor foi {min(lista)}')
