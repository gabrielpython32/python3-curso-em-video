'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
'''
from datetime import date
menoridade = 0
maioridade = 0
print('''*****************************
* Verificador de maioridade *
*****************************''')
qtd = int(input('\nDigite o número de pessoas para a análise: '))
for pessoa in range(1, qtd + 1):
    anonasc = int(input('\nInforme o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    if date.today().year - anonasc < 21:
        menoridade += 1
    else:
        maioridade += 1
print('\n{} pessoas são menores de idade.'.format(menoridade))
print('{} pessoas são maiores de idade.'.format(maioridade))
