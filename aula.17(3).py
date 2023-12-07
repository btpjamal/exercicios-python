a= [1,2,3,4]
b= a # aqui aconteceu a ligação
b[2]= 8
print(a)
print(b)
# as duas listas ficam iguais porque ouve uma ligação entre ambas

c= [5,6,7,8]
d= c[:] # faz com que receba uma cópia de todos os items
d[3]= 9
print(c)
print(d)