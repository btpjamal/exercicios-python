#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

lista_produtos= []
produtos_mais1000= 0
produto_mais_barato= None
preco_mais_barato= None
while True:
    produtos= {}

    produtos['nome']= str(input('Informe o nome do produto: '))
    produtos['preco']= float(input('Informe o preço do produto: '))
    lista_produtos.append(produtos)
    if produtos['preco'] > 1000:
        produtos_mais1000 +=1
    if preco_mais_barato is None or produtos['preco'] < preco_mais_barato:
        preco_mais_barato = produtos['preco']
        produto_mais_barato= produtos['nome']
    continuar= str(input('Deseja continuar?: '))
    if 's' in continuar.upper().lower():
        continue
    else:
        break
    
total_gasto= sum(produtos['preco'] for produtos in lista_produtos)  
print(f'''Fim do programa, o total gasto na compra foi de {total_gasto},
      foram ao total, {produtos_mais1000} produtos superiores a 1000 reais,
       e o produto mais barato é: {produto_mais_barato} ''')