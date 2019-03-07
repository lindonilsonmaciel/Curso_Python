"""Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços."""
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
# separando as palavras da frase na lista
junto = ''.join(palavras)
# removendo todos os espaços
inverso = junto[::-1]
# solução sem uso de for
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# invertendo a frase'''
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')