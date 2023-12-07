# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome_cidade= input('digite o nome da cidade: ')

verificador= 'santo' in nome_cidade.split()[0]

print(verificador)