"""Crie um algoritmo que leia um número e mostre
o seu dobro, seu triplo e raiz quadrada."""
num = int(input('Digite um valor inteiro: '))
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.2f}'.format(num, num+num, num*3, num**(1/2)))
