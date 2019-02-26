"""Crie um programa que leia o nome completo de uma pessoa
e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""
nome = input('Digite seu nome completo: ')
print('Nome em Maiúsculo: {}'.format(nome.upper()))
print('Nome em Minúsculo: {}'.format(nome.lower()))
letras = len(nome) - nome.count(' ')
print('Quantas letras tem(sem espaços)? {}'.format(letras))
espaco = nome.find(' ')
print('Primeiro nome: {}'.format(nome[:espaco]))