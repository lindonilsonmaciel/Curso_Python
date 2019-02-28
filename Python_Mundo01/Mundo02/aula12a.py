nome = input('Qual é o seu nome? ')
if nome == 'Lindonilson':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}'.format(nome))