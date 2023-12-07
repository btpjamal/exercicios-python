# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

produto= float(input('Informe o valor do produto: '))

#formas de pagamento

vista= produto - produto * 10/100
vista_cartao= produto - produto * 5/100
cartao2x= produto / 2
cartao3x= (produto / 3 + produto * 20/100)

select=int(input('''ESCOLHA UMA FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
[5] pagamento parcelado
'''))

if select == 1:
    print(f'Sua forma de pagamento é à vista, o valor fica em: {vista}')
elif select == 2:
    print(f'Sua forma de pagamento é a vista no cartão, o valor fica em: {vista_cartao}')
elif select == 3:
    print(f'Sua forma de pagamento é em 2x no cartão, o valor fica em: {cartao2x}')
elif select == 4:
    print(f'Sua forma de pagamento é em 3x no cartão, o valor fica em: {cartao3x:.2f}')
elif select == 5:
    print('Você escolheu parcelar em mais de 3x')
    qtd_parcelas = int(input('Informe a quantidade de parcelas: '))
    parcelas = (produto / qtd_parcelas + produto * 20 / 100)
    print(f'O valor ficou em: {parcelas}')
else:
    print('número invalido...')