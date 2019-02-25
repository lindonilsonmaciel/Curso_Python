"""Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa."""
opo = float(input('Digite o cumprimento do cateto oposto: '))
adj = float(input('Digite o compimento do cateto adjacente: '))
hipo = (opo**2 + adj**2)**(1/2)
# import math
# math.hypot(opo,adj)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
