lanche= ('hambúrguer','suco','pizza','pudim')
print(lanche[1:3]) # o fatiamento do indice 1 até o indice 3, ignorando o indice 3

# [:] no fatiamento, o numero antes dos dois pontos indica de qual indice queremos começar,
# o numero após os dois pontos, aonde queremos terminar, lembrando que ele sempre deixa de fora esse número
# ex: no fatiamento [1:3], começou no indice 1 e foi até o 3, porém o 3 fica de fora
# mostrando assim apenas os items que estiverem nos indices 1 e 2
print(f'fatiamento começando do indice 2 e indo até o final: {lanche[2:]}')
print(f'fatiamento começando do começo, e indo até o indice 2, ignorando ele mesmo: {lanche[:2]}')

for i in range(len(lanche)): # o "len" do python é o "length" do javascript, usa da mesma forma
    print(lanche[i])

#for i in lanche:
#    print(i)

print(sorted(lanche)) # é o "sort" do javascript

