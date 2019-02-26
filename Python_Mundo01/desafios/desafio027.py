"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""
nome = input('Digite seu nome: ').strip()
posI = nome.find(' ')
posF = nome.rfind(' ')
print('Seu primeiro nome é {}'.format(nome[:posI]))
print('Seu último nome é {}'.format(nome[posF:]))
# Outra forma de responder é usando split, pegando o spli na posição
# 0 e depois na posição example[len(example)-1]
