"""Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas."""

km = int(input('Qual a distância em km? '))
valor = 0
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.5
print('O valor da passagem é R$ {:.2f}'.format(valor))