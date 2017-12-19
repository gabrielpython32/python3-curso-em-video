'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execição, mostre
a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar
se o usuário quer ou não continuar a digitar os valores.
'''

continuar = 's'
soma = cont = media = maior = menor = 0

while continuar == 's':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]')).lower()

media = soma / cont

print('''Foram inseridos {} números, a média entre eles é {}.
O maior número é {} e o menor é {}.'''.format(cont, media, maior, menor))
