"""Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele
vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""

valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto é o seu salário? R$'))
tempo = int(input('Em quanto tempo pretende pagar? '))
prestacao = valor/(tempo*12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será R$ {:.2f}'.format(valor, tempo, prestacao))
if prestacao >= (salario*0.3):
    print('Empréstimo NEGADO!!')
else:
    print('Empréstimo CONCEDIDO!!')

