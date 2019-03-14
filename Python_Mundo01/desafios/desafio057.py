"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
 correto."""
sexo = input('Informe o Sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MmFf':
    print('Sexo Inválido!')
    sexo = input('Informe o Sexo [M/F]: ').strip().upper()[0]
print('Sexo Registrado Com Sucesso!!')