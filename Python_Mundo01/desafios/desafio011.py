"""Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados."""
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(largura, altura, area))
print('São necessários {:.2f}L de tinta para pintar a parede!'.format(area/2))