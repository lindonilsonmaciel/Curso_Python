"""Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos."""
peso = 0
maior = 0
menor = 0
for i in range(0,5):
    peso = float(input('Peso da {}º pessoa: '.format(i+1)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('A pessoa mais leve pesa {:.1f}kg e a mais pesada pesa {:.1f}kg'.format(menor, maior) )
