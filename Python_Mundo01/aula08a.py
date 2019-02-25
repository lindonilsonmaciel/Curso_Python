from math import sqrt,floor
# import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
# sqrt faz a raiz do número informado
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
#ceil arredonda para cima, floor para baixo
