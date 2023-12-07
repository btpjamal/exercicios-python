# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase= str(input('Digite uma frase: '))
contador= frase.upper().lower().count('a')
posicao= frase.upper().lower().strip().find('a')
ultima= frase.upper().lower().strip().rfind('a')
print(f'''A letra apareceu {contador} vezes, nas posições {posicao} e {ultima}''')