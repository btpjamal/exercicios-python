#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms= float(input('informe a kilometragem percorrida com o veiculo: '))
dias= int(input('informe a quantidade de dias alugados: '))

dia= 60
km= 0.15
conta_kms= kms * km
conta_dias= dias * dia
conta_total= conta_dias + conta_kms

print(f'''O veiculo percorreu {kms} kms
Foi alugado por {dias} dias

O valor ficará em {conta_total}''')
