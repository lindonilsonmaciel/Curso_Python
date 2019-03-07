"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do
homem mais velho e quantas mulheres têm menos de 20 anos."""

nome = ''
idade = 0
sexo = ''
total = 0
maisVelho = 0
mulheres = 0
homemVelho = ''

for i in range(0,4):
    print('-' * 5, ' {} PESSOA '.format(i+1), '-' * 5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ')
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    if sexo in 'Mm':
        if i == 1:
            maisVelho = idade
            homemVelho = nome
        elif maisVelho < idade:
            maisVelho = idade
            homemVelho = nome
    total += idade

print('A média de idade do grupo é de {:.1f} anos'.format(total/4.0))
print('O homem mais velho tem {} anos e se chama {}'.format(maisVelho, homemVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
