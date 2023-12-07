#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto= float(input('digite o valor do produto: '))
desconto= produto - (produto*5/100)   # 5/100
                                      # 5 por 100
                                      # 5 por cento

print(f'O valor do desconto foi de 5%, o novo valor é de:{desconto}')