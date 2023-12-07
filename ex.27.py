# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome= str(input('Nome: '))
primeiro_nome= nome.split()[0]
ultimo_nome= nome.split()[-1]
print(f'''{primeiro_nome} {ultimo_nome}''')