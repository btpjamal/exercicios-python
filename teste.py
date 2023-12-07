from random import randint
lista= []

for i in range(100):
    valores= randint(500,600)
    while True:
        if valores not in lista:
            lista.append(valores)
            break
        else:
            valores= randint(500, 600)
            continue

print(sorted(lista))

multiplos_dez= []

for i in range(100):
    valores= randint(500,600)
    if valores %10 == 0:
        multiplos_dez.append(valores)

print(sorted(multiplos_dez))

pares= 0
for i in range(len(lista)):
    if lista[i]%2==0 and lista[i+ 1]%2==0:
        pares+= 1
print(f'a quantidade de pares é {pares}')

