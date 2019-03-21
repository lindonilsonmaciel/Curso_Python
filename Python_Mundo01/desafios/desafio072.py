"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso."""
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if escolha >= 0 and escolha <= 20:
        print('Você digitou o número {}'.format(extenso[escolha]))
        break
    else:
        escolha = int(input('Digite um número entre 0 e 20: '))