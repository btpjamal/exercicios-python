# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome= str(input('Nome: '))
nome_maiusculo= nome.upper()
nome_minusculo= nome.lower()
quant_letras= nome.strip().__len__() - nome.count(' ')   # .count() elimina oq pedir pra contar dentro do parametro
primeiro= nome.split()[0].__len__()  # o primeiro nome é o elemento zero da lista

print(f'''O nome com todas as letras maiusculas fica: {nome_maiusculo}
O nome com todas as letras minusculas: {nome_minusculo}
A quantidade de letras, desconsiderando os espaços: {quant_letras}
A quantidade de letras do primeiro nome: {primeiro}''')