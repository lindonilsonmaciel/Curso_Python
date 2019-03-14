"""Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag)."""
n = int(input('Digite um número [999 para parar]: '))
c = 0
soma = 0
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número(s) e a soma entre ele(s) foi {}'.format(c, soma))