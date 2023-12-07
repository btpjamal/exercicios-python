a= (3,3,4,7,8)
b= (4,5,6,7)
c= a + b
print(c)
print(c.count(3)) # "count() para contar quantas vezes um elemento aparece dentro da lista"
print(c.index(6)) # "index() para mostrar o indice do elemento especificado"
print(c.index(7)) # retornou o resultado "3", pois averigou a primeira ocorrencia onde encontrou o numero
print(c.index(7,4)) # retornou o resultado "8", pois averigou a partir da posição "4", especificada após a virgula

