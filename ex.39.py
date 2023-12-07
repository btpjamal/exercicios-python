# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime
ano_nascimento= int(input('Informe seu ano de nascimento: '))
ano_atual= datetime.now().year
idade= ano_atual - ano_nascimento
print(f'''Quem nasceu em {ano_nascimento}, atualmente já tem: {idade}''')

if idade < 18:
    saldo = 18 - idade
    print(f'''Você ainda não possui 18 anos, ainda não chegou a hora de se alistar...
ainda restam {saldo} anos para seu alistamento''')
elif idade > 18:
    saldo= idade - 18
    print(f'''Você já é maior de 18 e já passou do prazo de se alistar!!!, deveria ter se alistado em {saldo} anos,
seu alistamento ocorreu em {ano_nascimento + 18}''')
else:
    print(f'''Já está na hora de se alistar!!!, atualmente você possui {idade} anos''')