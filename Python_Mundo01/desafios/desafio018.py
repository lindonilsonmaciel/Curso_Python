"""Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo."""
import math
ang = int(input('Digite o angulo a se calcular: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}, Coseno de {:.2f} e a Tangente de {:.2f}'.format(ang, sen, cos, tan))
