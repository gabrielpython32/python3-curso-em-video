'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$ 10 e R#1.
'''

print('''**********************************************
*      Caixa Eletrônico - Banco Maroto       *
**********************************************''')

cont50 = cont20 = cont10 = cont1 = 0

valor_sacado = int(input('Quanto você deseja sacar? R$'))

while valor_sacado is not 0:

    if valor_sacado >= 50:
        cont50 += 1
        valor_sacado -= 50

    elif valor_sacado >= 20:
        cont20 += 1
        valor_sacado -= 20

    elif valor_sacado >= 10:
        cont10 += 1
        valor_sacado -= 10

    elif valor_sacado < 10:
        cont1 += 1
        valor_sacado -= 1

print(f'''**********************************************
Total de {cont50} cédulas de R$50,00
Total de {cont20} cédulas de R$20,00
Total de {cont10} cédulas de R$10,00
Total de {cont1} cédulas de R$1,00
**********************************************
Obrigado por usar os serviços do Banco Maroto.
**********************************************''')
