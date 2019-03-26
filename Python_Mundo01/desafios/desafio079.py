"""Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente. """
valores = list()
resp = 'a'
num = 0
while True:
    num = int(input('Digite um Valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('O Valor Já Existe, Portanto Não Foi Adicionado!!')
    resp = 'a'
    while resp not in 'SN':
        resp = input('Quer Continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
print('Você digitou os valores {}'.format(valores))