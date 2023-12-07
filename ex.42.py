# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


reta1= int(input('RETA 1: '))
reta2= int(input('RETA 2: '))
reta3= int(input('RETA 3: '))


equilatero= reta1 == reta2 == reta3

isosceles= reta1 == reta2 != reta3

escaleno= reta1 != reta2 != reta3

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode formar um triangulo')
    if equilatero:
        print('Formará um triangulo equilátero')
    elif isosceles:
        print('Formará um triangulo isósceles')
    elif escaleno:
        print('Formará um triangulo escaleno')
else:
    print('Não pode formar um triangulo')