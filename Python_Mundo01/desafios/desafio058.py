"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
#faz o computador esperar por alguns segundos
computador = randint(0,10)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
tentativas = 1
while jogador != computador:
    tentativas += 1
    sleep(0.5)
    if jogador < computador:
        jogador = int(input('Mais... Tente mais uma vez:'))
    else:
        jogador = int(input('Menos... Tente mais uma vez:'))
print('Acertou com {} tentativas. PARABÉNS!'.format(tentativas))
