"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=-'*30)
print('Times do Brasileirão')
print(times)
print('=-'*30)
print('5 Primeiros Colocados')
print('=-'*30)
print(times[0:5])
print('=-'*30)
print('4 Últimos Colocados')
print('=-'*30)
print(times[-4:])
print('=-'*30)
print('Times em Ordem Alfabética')
print(sorted(times))
print('=-'*30)
print('Em Qual Posição Está a Chapecoense?')
print(times.index('Chapecoense')+1)

