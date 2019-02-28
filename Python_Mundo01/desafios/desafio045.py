"""Crie um programa que faça o computador jogar Jokenpô com você."""

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
j1 = int(input('>>> '))
j2 = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

# Jogada Inválida
if j1 > 2:
    print('JOGADA INVÁLIDA!!!')

# Joguei 0
elif j1 == 0 and j2 == 2:
    print('-='*10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você GANHOU!!')
elif j1 == 0 and j2 == 1:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você PERDEU!!')
elif j1 == 0 and j2 == 0:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('EMPATE!!')

# Joguei 1
elif j1 == 1 and j2 == 0:
    print('-='*10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você GANHOU!!')
elif j1 == 1 and j2 == 2:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você PERDEU!!')
elif j1 == 1 and j2 == 1:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('EMPATE!!')

# Joguei 2
elif j1 == 2 and j2 == 1:
    print('-='*10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você GANHOU!!')
elif j1 == 2 and j2 == 0:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('Você PERDEU!!')
elif j1 == 2 and j2 == 2:
    print('-=' * 10)
    print('Você escolheu {}'.format(itens[j1]))
    print('O computador escolheu {}'.format(itens[j2]))
    print('-=' * 10)
    print('EMPATE!!')