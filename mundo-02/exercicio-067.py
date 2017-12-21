'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    n = int(input('\nDigite um número para verificar sua tabuada: '))
    print()
    if n < 0:
        break
    for x in range(0, 11):
        res = n * x
        print(f'{n} X {x} = {res}')

print('Programa encerrado.')
