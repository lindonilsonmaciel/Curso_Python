"""Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do
tempo do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo."""
ano = int(input('Ano de nascimento: '))
anoA = 2019
# date.today().year / Para pegar o ano atual
print('Quem nasceu em {} tem {} anos em {}'.format(ano, anoA-ano, anoA))
if anoA - ano <= 18:
    print('Falta ainda {} para poder se alisar'.format(18-(anoA - ano)))
elif anoA - ano == 18:
    print('Está na hora de se alistar, corre lá!')
else:
    print('Você devia ter se alistado há {} anos atrás.'.format((anoA - ano)-18))