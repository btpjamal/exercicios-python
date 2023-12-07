# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero= int(input('Número: '))

unidade=numero // 1 % 10 # resto da divisão por 1, retira o módulo de 10

dezena=numero // 10 % 10 # resto da divisão por 10, retira o módulo de 10

centena=numero // 100 % 10 # resto da divisão por 100, retira o módulo de 10

milhar=numero // 1000 % 10 # resto da divisão por 1000, retira o módulo de 10

print(f'''
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
''')