#Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.
import math

raio= float(input('informe o raio do círculo: '))
area= math.pi * raio**2
#P = 2πr
perimetro= (2*math.pi+raio)

print(f'O perimetro é: {perimetro:.2f}, a área é: {area:.2f}')
