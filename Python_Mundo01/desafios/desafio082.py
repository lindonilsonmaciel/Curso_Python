"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas."""
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
print('=-'*25)
pares = list()
impares = list()
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(pares))
print('A lista de impares é {}'.format(impares))