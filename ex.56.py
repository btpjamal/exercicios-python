# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


pessoas= int(input('informe a quantidade de pessoas a serem analisadas: '))
homems= []
mulheres= []
mulheres_menos_20= 0
for i in range(pessoas):
    nome= input('Nome: ')
    idade= int(input('Idade: '))
    sexo= input('sexo (m ou f): ')
    rg= nome, idade, sexo
    media = idade * pessoas / pessoas
    if sexo == 'm':
        homems.append(rg)
    elif sexo == 'f':
        mulheres.append(rg)


print(f'{homems}')
homem_mais_velho= max(homems, key=lambda homem: homem[1])
print(f'Dentre os homems, o mais velho é {homem_mais_velho[0]} com {homem_mais_velho[1]} anos')
print(f'{mulheres}')
if idade < 20 and sexo == 'f':
    mulheres_menos_20 += 1
    print(f'Existem,{mulheres_menos_20} mulheres com menos de 20 anos')
print(media)



