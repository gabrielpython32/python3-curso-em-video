# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -> O primeiro valor é maior
# -> O segundo valor é maior
# -> Não existe valor maior, os dois são iguais.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior.'.format(n1))
elif n2 > n1:
    print('O número {} é maior.'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
