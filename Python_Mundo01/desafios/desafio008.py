"""Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros."""
metros = float(input('Digite um valor em metros: '))
print('{}m equivale à {}cm e {}mm'.format(metros, metros*100, metros*1000))
