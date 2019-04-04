"""Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = list()
pessoa = list()
resp = 'a'
pesada = 0
leve = 0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesada = leve = pessoa[1]
    else:
        if pessoa[1] > pesada:
            pesada = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = 'a'
    while resp not in 'SN':
        resp = input('Quer Continuar? [S/N] ').upper()
    if resp == 'N':
        break;
print('=-'*20)
print('Ao todo você cadastrou {} pessoa(s)'.format(len(pessoas)))
print('A pessoa mais leve tem {:.2f}Kg, peso de '.format(leve), end='')
for p in pessoas:
    if p[1] == leve:
        print(p[0], ' ', end='')
print()
print('A pessoa mais pesada tem {:.2f}Kg, peso de '.format(pesada),end='')
for p in pessoas:
    if p[1] == pesada:
        print(p[0], ' ', end='')