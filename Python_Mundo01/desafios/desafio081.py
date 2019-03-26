"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
lista = list()
resp = 'a'
while True:
    num = int(input('Digite um Valor: '))
    lista.append(num)
    resp = 'a'
    while resp not in 'SN':
        resp = input('Quer Continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
print('Você Digitou {} Elementos.'.format(len(lista)))
lista.sort(reverse=True)
print('Os Valores em Ordem Descrescente São {}'.format(lista))
if 5 in lista:
    print('O Valor 5 Está Presente na Lista!')
else:
    print('O Valor 5 Não Está Presente na Lista!')