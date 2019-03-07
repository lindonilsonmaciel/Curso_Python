"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
print('='*26)
print('   10 TERMOS DE UMA PA')
print('='*26)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
t2 = t1 + 10 * razao
for i in range(t1,t2, razao):
    print(i, end=' -> ')

print('ACABOU')