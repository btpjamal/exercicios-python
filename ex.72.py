tupla= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero= int(input('digite um número de 0 a 20: '))

while numero < 0 or numero > 20:
    print('número inválido, digite novamente')
    numero= int(input('digite um número de 0 a 20: '))

print(f'Voce digitou o número {tupla[numero]}')
    
    
