# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Registre seu peso: '))
altura= float(input('Registre sua altura: '))

imc= peso / (altura ** 2)
print(f'Seu IMC é de: {imc:.2f}, este calculo não leva em consideração a distribuição de massa muscular ou de gordura')

if imc < 18.5:
    print('Você está abaixo do Peso')
elif imc >= 18.5 and imc < 25.0:
    print('Você está dentro do seu Peso Ideal')
elif imc >= 25.0 and imc < 30.0:
    print('Você está com Sobrepeso')
elif imc >= 30.0 and imc < 40.0:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')