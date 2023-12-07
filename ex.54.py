# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
pessoas_maior_idd= []
pessoas_menor_idd= []
data= datetime.datetime.now().year


for i in range(7):
    ano_nascimento= int(input('informe o ano de nascimento: '))
    print(f'Você possui {data - ano_nascimento} anos')
    idade= data - ano_nascimento
    if idade >= 18 :
        pessoas_maior_idd.append(idade)
    else:
        pessoas_menor_idd.append(idade)

print(pessoas_maior_idd)
print(pessoas_menor_idd)
