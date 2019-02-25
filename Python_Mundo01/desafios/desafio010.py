"""Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar."""
cash = float(input('Quanto tem em R$ na carteira?'))
print('R$ {:.2f} é quivalente à U$ {:.2f}'.format(cash, cash/3.73))