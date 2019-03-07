"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores."""
from datetime import date
ano = 0
atual = date.today().year - 18
maior = 0
menor = 0
for i in range(0,7):
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(i+1)))
    if ano < atual:
        maior += 1
    else:
        menor += 1

print('Ao todo temos {} maiores de idade e {} menores de idade'.format(maior,menor))