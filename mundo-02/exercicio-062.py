'''
Melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('Progressão aritimética')

n1 = int(input('Informe o primeiro termo: '))
rz = int(input('Informe a razão da PA: '))
nn = int(input('Informe a quantidade de termos: '))

cont = 0

print('\nO resultado da progressão de {} com razão {} e com {} elementos é:\n'.format(n1, rz, nn))

print('{} ->'.format(n1), end=' ')

while nn != 0:
    nn += cont - 1
    while cont <= nn:
        cont += 1
        n1 += rz
        print('{} ->'.format(n1), end=' ')
    print('FIM')
    nn = int(input('\nInforme a quantidade de termos para ver a partir desses: '))

print('\nNo total, foram vistos {} termos.'.format(cont))

print('\nFim do cálculo da PA.')
