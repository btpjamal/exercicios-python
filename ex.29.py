#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc_carro= int(input('Registre a velocidade do veiculo: '))
radar= 80
multa= (veloc_carro - radar) * 7


if veloc_carro > radar:
    print(f'Você foi multado por transitar acima de {radar}, multa de: {multa:.2f}')