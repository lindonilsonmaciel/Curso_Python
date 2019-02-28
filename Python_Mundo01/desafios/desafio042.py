"""Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois
lados iguais, um diferente - ESCALENO: todos os lados diferentes"""
s1 = int(input('Segmento 1: '))
s2 = int(input('Segmento 2: '))
s3 = int(input('Segmento 3: '))

if s1 < s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')

