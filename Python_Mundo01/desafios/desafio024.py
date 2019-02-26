"""rie um programa que leia o nome de uma cidade diga
se ela começa ou não com o nome "SANTO"."""
city = input('Digite o nome de sua cidade: ')
pos = city.strip().find(' ')
print('SANTO' in city.strip()[:pos].upper())

# Outra solução
# city = input('Digite o nome de sua cidade: ').strip
# print(city[:5].upper() == "SANTO")