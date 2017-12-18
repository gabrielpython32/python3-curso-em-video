'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

sair = 'n'

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('\nDigite outro número qualquer: '))

while sair == 'n':

    menu = int(input('''\nOperações disponíveis:
\n[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
\nSelecione a operação desejada: '''))

    if menu == 1:
        soma = n1 + n2
        print('O resultado da soma entre {} e {} é igual a {}.'.format(n1, n2, soma))

    elif menu == 2:
        mult = n1 * n2
        print('O valor da multiplicação entre {} e {} é igual a {}.'.format(n1, n2, mult))

    elif menu == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 == n2:
            print('Os números {} e {} são iguais.'.format(n1, n2))
        else:
            print('O maior número é {}.'.format(n2))

    elif menu == 4:
        n1 = int(input('\nDigite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

    elif menu == 5:
        sair = str(input('\nTem certeza que deseja sair? [S/N]')).lower()

    else:
        print('\nOpção inválida. Tente novamente.')
        sleep(4)
