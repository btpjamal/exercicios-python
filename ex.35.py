# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

reta1= int(input('Primeira reta: '))
reta2= int(input('Segunda reta: '))
reta3= int(input('terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'Pode formar um triangulo')

else:
    print(f'Não pode formar um triangulo')
