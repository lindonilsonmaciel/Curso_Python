# basicamente o comando é
# \033[style;text;background m - substituindo esses nomes por número
# \033[0;33;44m exemplo - obs: são opcionais e podem vir em qualquer posição
# style: 0 (none), 1 (negrito), 4 (sublinhado), 7 (negativo)
# text: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(cinza)
# back: mesmas cores, começando com 4 ao invés de 3, 40, 41, 42, 43, 44, 45, 46, 47

print('\033[1;31;43mOlá Mundo\033[m') #Fonte negrito Letras Vermelhas,Fundo amarelo. por fim volta ao normal
# print('Teste {} mudou de cor {}'.format('\033[m','\033[,')) # da pra se usar no format também