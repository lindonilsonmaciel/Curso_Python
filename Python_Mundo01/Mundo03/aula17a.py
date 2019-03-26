num = [2,5,9,1]
num[2] = 3
num.append(7)
# adiciona
num.sort(reverse=True)
#coloca na ordem do menor para maior
num.insert(2, 2)
if 4 in num:
    num.remove(4)
# excluí um item da lista
print(num)