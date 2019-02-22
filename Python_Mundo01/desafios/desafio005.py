"""Faça um programa que leia um número inteiro
e mostre na tela o seu antecessor e o seu sucessor."""
num = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e o seu sucessor é {}'.format(num, num-1, num+1))