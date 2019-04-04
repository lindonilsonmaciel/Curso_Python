"""Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
numeros = [[], []]
for i in range(0,7):
    n = int(input('Digite o {}º valor: '.format(i+1)))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('Os valores pares digitados foram {}'.format(sorted(numeros[0])))
print('os valores impares digitados firam {}'.format(sorted(numeros[1])))