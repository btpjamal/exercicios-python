# Crie um programa que informe se o ano é ou não, um ano bissexto

from datetime import date
ano= int(input('Insira um ano, para inserir o ano atual, selecione 0... : '))

if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano}, é BISSEXTO')
else:
    print(f'O ano {ano}, NÃO É BISSEXTO')
