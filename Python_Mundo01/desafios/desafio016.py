"""Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira."""
from math import trunc
real = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(real, trunc(real)))
