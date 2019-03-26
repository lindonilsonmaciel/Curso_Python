"""aça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista. """
num = list()
for v in range(0,5):
    num.append(int(input('Digite um valor para a Posição {}: '.format(v))))
print('=-'*20)
print('Você digitou os valores {}'.format(num))
print('O maior valor digitado foi {} na(s) posição(ões) '.format(max(num)), end='')
for i, v in enumerate(num):
    if v == max(num):
        print('{}...'.format(i), end='')
print('\nO menor valor digitado foi {} na(s) posição(ões) '.format(min(num)), end='')
for i, v in enumerate(num):
    if v == min(num):
        print('{}...'.format(i), end='')
