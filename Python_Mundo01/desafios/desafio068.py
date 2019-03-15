"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. """
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
vitorias = 0
while True:
    computador = randint(0,9)
    jogador = int(input('Diga um Valor: '))
    jogada = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    print('-'*40)
    soma = 0
    soma = computador + jogador
    if jogada in 'Pp':
        if soma % 2 == 0:
            print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(jogador, computador, soma))
            print('-'*40)
            print('Você VENCEU!!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        else:
            print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(jogador, computador, soma))
            print('-'*40)
            print('Você PERDEU!')
            print('=-' * 20)
            break
    elif jogada in 'Ii':
        if soma % 2 != 0:
            print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR'.format(jogador, computador, soma))
            print('-'*40)
            print('Você VENCEU!!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        else:
            print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(jogador, computador, soma))
            print('-' * 40)
            print('Você PERDEU!')
            print('=-' * 20)
            break
print('GAME OVER! Você venceu {} veze(s)'.format(vitorias))
