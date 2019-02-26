"""Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que
posição ela aparece a primeira vez e em que posição
ela aparece a última vez."""
nome = input('Digite seu nome: ').strip()
print('Quantas vezes aparece a letra A: {}'.format(nome.upper().count('A')))
print('Qual a primeira ocorrencia da letra A: {}'.format(nome.upper().find('A')))
print('Qual a ultima ocorrencia da letra A: {}'.format(nome.upper().rfind('A')))
