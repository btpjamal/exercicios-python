#lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo = primeiro
contador = 1
total= 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais= int(input('quantos termos quer mostrar a mais?: '))
print(f'FIM, {total} termos mostrados')

