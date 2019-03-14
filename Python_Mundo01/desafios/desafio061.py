"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma
PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""
print('='*26)
print('   10 TERMOS DE UMA PA')
print('='*26)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    print('{}'.format(t1), end=' -> ')
    t1 += razao
    c += 1

print('ACABOU')