"""Escreva um programa que leia a velocidade de um
carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00
por cada Km acima do limite."""

km = int(input('Qual a velocidade do seu carro? '))
if km > 80:
    print('Você foi multado!!')
    print('Multa no valor de R$ {}'.format((km-80)*7))
else:
    print('Velocidade normal, pode seguir viagem!!')