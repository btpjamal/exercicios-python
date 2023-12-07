# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome= str(input('Nome: '))

verificador= 'silva' in nome.upper().lower() # verifica em maiusculo e minusculo

print(verificador)