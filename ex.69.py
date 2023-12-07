# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

lista_pessoas= []
maior_18= 0
homens= 0
mulheres_menor_20= 0
while True:
    pessoa = {}

    pessoa['nome']= str(input('Informe o nome: '))
    pessoa['idade']= int(input('Informe a idade: '))
    pessoa['sexo']= str(input('Informe o sexo (M/F): '))
    
    lista_pessoas.append(pessoa)

    print(lista_pessoas)
    
    if pessoa['idade'] >= 18:
        maior_18 += 1
    if pessoa['sexo'].upper().lower() == 'm':
        homens+=1
    if pessoa['idade'] < 20 and pessoa['sexo'].upper().lower() == 'f':
        mulheres_menor_20 +=1
    continuar= str(input('Deseja continuar?: '))
    if 's' in continuar.upper().lower():
        continue
    else:    
        break
print(f'''Fim do programa, com {maior_18} pessoas maiores de 18 anos,
{homens} homens, e {mulheres_menor_20} mulheres com menos de 20 anos ''')



