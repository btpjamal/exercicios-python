#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
valor1= int(input('Valor 1: '))
valor2= int(input('Valor 2: '))
lista_check_maior= []

opcoes= int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))

while True:
    if opcoes == 1:
        print(f'A soma entre {valor1} + {valor2} resulta em {valor1 + valor2}')
        opcoes= int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
        continue
    elif opcoes == 2:
        print(f'A multiplicação entre {valor1} * {valor2} resulta em {valor1 * valor2}')
        opcoes= int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
        continue
    elif opcoes == 3:
        lista_check_maior.append(valor1)
        lista_check_maior.append(valor2)
        print(f'O maior valor é {max(lista_check_maior)}')
        opcoes= int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
        continue
    elif opcoes == 4:
        lista_check_maior= []
        valor1= int(input('digite um novo valor: '))
        valor2= int(input('digite um novo valor: '))
        opcoes= int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''))
        continue
    elif opcoes == 5:
        print('Programa encerrado')
        break
