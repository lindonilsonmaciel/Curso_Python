"""Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR."""

num = int(input('Digite um valor qualquer: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número é {} ímpar'.format(num))