frase= input('digite algo: ')
vogais= 0
for c in frase:                        # para cada caractere em "frase"
    if c in 'a,e,i,o,u':               # se "caractere" for 'a,e,i,o,u':
        vogais += 1                    # adicione 1 na contagem das vogais

print(vogais)