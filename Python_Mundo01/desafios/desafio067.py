"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo. """
while True:
    t = int(input('Qual tabuada deseja fazer? '))
    print('-'*30)
    if t < 0:
        break
    c = 1
    for i in range(1,11):
        print('{} x {} = {}'.format(i, t, i*t))
    print('-'*30)
print('Tabuada Encerrada!!!')