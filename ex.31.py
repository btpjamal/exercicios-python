# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem= float(input('Informe a distacia da viagem: '))

if viagem <= 200:
    passagem= viagem * 0.50
    print(f'A passagem custará: {passagem}')
else:
    passagem_longa= viagem * 0.45
    print(f'A passagem custará: {passagem_longa}')