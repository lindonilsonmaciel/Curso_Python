"""Escreva um programa que converta uma temperatura digitando
 em graus Celsius e converta para graus Fahrenheit."""
celsius = float(input('Digite a temperatura em Cº: '))
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF'.format(celsius, (celsius*9/5)+32))
