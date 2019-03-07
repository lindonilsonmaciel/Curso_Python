"""Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo."""
n = int(input('Digite um número: '))
cont = 0
for i in range(1,n+1):
    if n % i == 0:
        print('{}{}{}'.format('\033[33m', i, '\033[33m'), end=' ')
        cont += 1
    else:
        print('{}{}{}'.format('\033[31m', i, '\033[31m'), end=' ')

if cont == 2:
    print('\n\033[mO número {} É PRIMO'.format(n))
else:
    print('\n\033[mO número {} NÃO É PRIMO'.format(n))