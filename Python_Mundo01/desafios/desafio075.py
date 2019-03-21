"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
print('Digite 4 Valores: ')
n = (int(input()),int(input()),int(input()),int(input()))
print('='*25)
print('Quantas Vezes Apareceu o Valor 9? {}'.format(n.count(9)))
if 3 in n:
    print('Em Que Posição Foi Digitado o Valor 3? {}ª'.format(n.index(3)+1))
else:
    print('O Valor 3 Não Foi Digitado!')
print('Quantos Números Pares Foram Digitados? ',end='')
cont = 0
for i in n:
    if i % 2 == 0:
        cont += 1
print(cont)
