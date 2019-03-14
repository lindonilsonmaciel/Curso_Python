"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""
n = int(input('Digite um Valor Para Fatorar: '))
fat = 1
print('Calculando {}! = {}'.format(n, n), end='')
while n > 1:
    fat *= n
    n -= 1
    if n == 1:
        print(' x 1 = ', end='')
    else:
        print(' x {}'.format(n), end='')
print(fat)