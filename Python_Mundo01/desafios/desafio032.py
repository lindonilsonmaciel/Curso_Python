"""Faça um programa que leia um ano qualquer e
mostre se ele é bissexto."""

ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))

if ano == 0:
    ano = 2019
    if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
        print('O ano de {} é bissexto'.format(ano))
    else:
        print('O ano {] não é bissexto!'.format(ano))
else:
    if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
        print('O ano de {} é bissexto'.format(ano))
    else:
        print('O ano {} não é bissexto!'.format(ano))