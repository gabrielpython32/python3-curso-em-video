'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
peso_lista = []
print('''***********************
* Comparador de pesos *
***********************\n''')
for pessoas in range(1, 6):
    peso = int(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    peso_lista.append(peso)
print('\nO peso menor foi: {}'.format(min(peso_lista)))
print('O peso maior foi: {}'.format(max(peso_lista)))
