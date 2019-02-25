"""Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço, com 5% de desconto."""
preco = float(input('Digite o preço do produto: R$ '))
print('Seu produto com 5% de desconto tem seu novo preço de R$ {:.2f}'.format(preco-(preco*0.05)))
