'''
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5x4x3x2x1 = 120
'''

# Farei esse exercício usando os dois modos: for e while.

print('Cálculo do fatorial de um número.\n')

n = int(input('Digite um número para saber seu fatorial: '))

fat = 1

print('\nO fatorial de {} ({}!) é:'.format(n, n), end=' ')

'''
# Essa é a solução usando o 'for':
for x in range(n, 0, -1):
    fat *= x
    print(x, ' X ' if x > 1 else ' = ', end=' ')

print('{}'.format(fat))
'''

# Essa é a solução usando 'while':
while n > 0:
    fat *= n
    n -= 1
    print(n + 1, ' X ' if n > 0 else ' = ', end=' ')

print('{}'.format(fat))
