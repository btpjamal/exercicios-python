#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo= str(input('Informe seu sexo (M/F): '))

while True:
    if sexo == 'm':
        print('Sexo masculino registrado')
        break
    elif sexo == 'f':
        print('Sexo feminino registrado')
        break
    else:
        print('digite novamente...')
        sexo= str(input('Informe seu sexo (M/F): '))
        continue
