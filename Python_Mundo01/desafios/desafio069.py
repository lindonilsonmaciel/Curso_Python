"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

maiores = homens = mulheres = 0
while True:
    print('-'*40)
    print('     CADASTRE UMA PESSOA     ')
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        print('-' * 40)
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    esc = ' '
    if esc not in 'SN':
        esc = input('Quer Continuar? [S/N]').strip().upper()[0]
    if esc == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(maiores))
print('Ao todo temos {} homen(s) cadastrados'.format(homens))
print('E temos {} mulhere(s) com menos de 20 anos'.format(mulheres))