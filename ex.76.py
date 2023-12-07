produtos= {}

tamanho= int(input('Quantos produtos quer adicionar?: '))


for i in range(tamanho):
    add_produto= str(input('adicinar produto: '))
    add_preco= float(input('adicionar preço: '))
    produtos[add_produto] = add_preco


print('Produto', '\t', 'Preço')
for produto, preco in produtos.items():
    print(produto, '\t', preco)