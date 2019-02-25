"""Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento."""
salario = float(input('Digite o seu salário: R$ '))
print('Seu novo salário com acrescimo de 15% fica de {:.2f}R$ para {:.2f}R$'.format(salario, salario+(salario*0.15)))
