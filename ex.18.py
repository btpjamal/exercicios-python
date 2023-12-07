#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan,radians  # é necessário converter os valores para radianos

angulo= float(input('valor do angulo: '))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))

print(f'''O seno é: {seno :.2f}
O cosseno é: {cosseno :.2f}
A tangente é: {tangente :.2f}''')