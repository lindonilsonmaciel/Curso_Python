"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for."""
n = int(input('Digite um valor para a tabuada: '))
for i in range(1,11):
    print('{:2} x {:2} = {:4}'.format(n, i, n*i))
