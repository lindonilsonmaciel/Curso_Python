"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20,
R$10 e R$1."""
print('='*40)
print('{:^40}'.format(' BANCO CEV '))
print('='*40)
valor = int(input('Que Valor Você Quer Sacar? R$'))
n50 = 0
n20 = 0
n10 = 0
n1 = 0
if valor > 50:
    print('Total de {} cédulas de R$50'.format(valor//50))
    valor = valor % 50
if valor > 20:
    print('Total de {} cédulas de R$20'.format(valor // 20))
    valor = valor % 20
if valor > 10:
    print('Total de {} cédulas de R$10'.format(valor // 10))
    valor = valor % 10
if valor >= 1:
    print('Total de {} cédulas de R$5'.format(valor // 5))
    valor = valor % 1
print('='*40)
print('Volte Sempre ao BANCO CEV! Tenha um Ótimo Dia!')

"""
Resposta de Guanabara
ced = 50 // variaveis que tem algum valor de inicio
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R${}'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
         ced = 10
        elif ced == 10:
            ced 1
        totced = 0
        if total == 0:
            break
"""