"""Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o."""
soma = 0
n = 0
for i in range(0,6):
    n = int(input('Digite o {} valor: '.format(i+1)))
    if n % 2 == 0:
        soma += n
    else:
        continue

print('A soma entre os valores pares digitados é {}'.format(soma))