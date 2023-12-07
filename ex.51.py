# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

p_a= int(input('Primeiro termo: '))
razao= int(input('razão: '))
decimo= p_a + (10 - 1) * razao   # fórmula matemática do décimo termo da progressão aritmética
for i in range(p_a, decimo + razao,razao):
    print(i)