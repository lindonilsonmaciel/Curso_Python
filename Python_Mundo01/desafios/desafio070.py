"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final,
mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """
total = 0.0
maisDeMil = 0
maisBaratoNome = 0.0
maisBarato = 0
opcao = ''
print('-'*40)
print('{:^40}'.format(' LOJA SUPER BARATÃO '))
print('-'*40)
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))

    total += preco
    if preco > 1000:
        maisDeMil += 1
    if maisBarato != 0:
        if preco < maisBarato:
            maisBaratoNome = produto
            maisBarato = preco
    else:
        maisBaratoNome = produto
        maisBarato = preco

    opcao = ' '
    if opcao not in 'SN':
        opcao = input('Quer Continuar Comprando [S/N]:').strip().upper()[0]
    if opcao == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produto(s) custando acima de R$1000.00'.format(maisDeMil))
print('O produto mais barato foi {} que custa R${:.2f}'.format(maisBaratoNome, maisBarato))