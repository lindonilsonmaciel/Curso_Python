"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import  sleep
esc = 0
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
while esc != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair')
    esc = int(input('>>> '))
    if esc == 1:
        print('{} + {} = {}'.format(n1,n2, n1+n2))
    elif esc == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif esc == 3:
        if n1 > n2:
            print('{} é o maior!'.format(n1))
        else:
            print('{} é o maior!'.format(n2))
    elif esc == 4:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
    elif esc == 5:
        print('FECHANDO...')
    else:
        print('Opcção INVÁLIDA!!')
    print('-='*10)
    sleep(2)
print('Fim do Programa, Volte Sempre!')