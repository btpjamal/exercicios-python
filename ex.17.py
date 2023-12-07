#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenunsa

from math import hypot

cateto_oposto= float(input('cateto oposto: '))
cateto_adjacente= float(input('cateto adjacente: '))
hipotenusa= hypot(cateto_oposto,cateto_adjacente)

print(f'''O comprimento da hipotenusa é de: {hipotenusa :.2f}''')