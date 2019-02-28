"""Escreva um programa em Python que leia um número
inteiro qualquer e peça para o usuário escolher qual será
a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
valor = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input())
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(valor, bin(valor)[2:]))
elif escolha == 2:
    print('{} convertido para BINÁRIO é igual a {}'.format(valor, oct(valor)[2:]))
elif escolha == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção Inválida!')