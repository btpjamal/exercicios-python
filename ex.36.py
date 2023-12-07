# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa= float(input('Informe o valor da casa: '))
salario_comprador= float(input('Informe o salário do comprador: '))
anos= int(input('Quantidade de anos para pagar: '))
prestacao= valor_casa / (anos * 12)
minimo= salario_comprador * 30 / 100

if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo não pode ser concedido')