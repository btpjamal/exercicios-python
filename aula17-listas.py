lista= [1,2,3,4,5]
lista[2]= 7 # alterei o indice 2, pelo número 7
print(lista)
lista.append(6) # o append(), adiciona o elemento ao final da lista
print(lista)
lista.sort() # o sort(), ordena a lista de forma crescente, ou alfabética
print(lista)
lista.sort(reverse=True) # usando o reverse=True, ordena de forma decrescente
print(lista)
lista.insert(0, 10) # insert(), para inserir um elemento em uma posição específica na lista, no indice 0, inseri o numero 10
print(lista)
print(len(lista)) # len() conta o comprimento da lista
# pop() ou remove() para remover um elemento da lista
# index() para mostrar o indice
# count() para contar quantas vezes um elemento aparece