"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar
0 termos."""
print('='*26)
print('   10 TERMOS DE UMA PA')
print('='*26)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
fim = 0
mais = 10
while mais != 0:
    fim += mais
    while c <= fim:
        print('{}'.format(t1), end=' -> ')
        t1 += razao
        c += 1

    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(fim))