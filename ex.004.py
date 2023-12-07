#Ele faz 20 km com 1 litro de combustível.
#Cada litro de combustível custa R$ 5,00.
#Faça um programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível ele pode comprar
#e quantos kilometros o carro consegue andar com este tanto de combustível.

combustivel = 5
kilometragem = 20

dinheiro= float(input('Qual o seu saldo atual?: '))


print(f'Com o seu saldo, é possível comprar {dinheiro/combustivel}litros, e percorrer {(dinheiro/combustivel)*kilometragem}')

