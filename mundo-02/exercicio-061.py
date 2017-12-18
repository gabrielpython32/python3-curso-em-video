'''
Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
'''

print('Progressão aritimética')

contador = 1

n1 = int(input('Informe o primeiro termo: '))
rz = int(input('Informe a razão da PA: '))
nn = int(input('Informe a quantidade de termos: '))

print('\nO resultado da progressão de {} com razão {} e com {} elementos é:\n'.format(n1, rz, nn))

print('{} ->'.format(n1), end=' ')

while contador <= nn:
    contador += 1
    n1 += rz
    print('{} ->'.format(n1), end=' ')

print('FIM')

print('\nFim do cálculo da PA.')
