#Faça um programa que leia a larga e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta para pintá-la, sabendo que cada litro de tinta preenche uma area de 2m

largura= float(input('largura da parede: '))
altura= float(input('altura da parede: '))
area= largura * altura
tinta= area / 2

print(f'serão necessarias {tinta} litros de tinta para preencher a area da parede')