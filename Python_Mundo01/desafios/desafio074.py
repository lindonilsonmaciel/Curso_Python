"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""
from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Eu sortiei os valores ', end='')
for i in n:
    print('{} '.format(i), end=' ')
print('\nO maior valor é {}'.format(max(n)))
print('O menor valor é {}'.format(min(n)))