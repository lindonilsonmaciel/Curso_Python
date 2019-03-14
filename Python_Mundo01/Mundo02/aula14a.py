"""
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
"""
esc = 0
r = 'S'
while r == 'S':
    esc = int(input())
    r = input('Quer continuar? ').upper()
print('FIM')