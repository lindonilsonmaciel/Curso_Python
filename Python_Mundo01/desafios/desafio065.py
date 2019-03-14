"""Crie um programa que leia vários números inteiros pelo teclado. No final
da execução, mostre a média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores."""
continuar = 'S'
media = menor = maior = soma = c = n = 0
while continuar in 'Ss':
    n = int(input('Digite um Número: '))
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    elif maior < n:
        maior = n
    elif menor > n:
        menor = n
    continuar = input('Quer continuar[S/N]: ').strip().upper()[0]
media = soma/c
print('Você digitou {} número(s) e a média foi {}'.format(c,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))