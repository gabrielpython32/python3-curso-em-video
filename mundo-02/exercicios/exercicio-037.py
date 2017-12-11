# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# [ 1 ] para binário
# [ 2 ] para octal
# [ 3 ] para hexadecimal
n = int(input('Digite um número inteiro para fazer a conversão: '))
print('''Selecione a opção abaixo:
[ 1 ] Para converter para BINÁRIO
[ 2 ] Para converter para OCTAL
[ 3 ] Para converter para HEXADECIMAL''')
menu = int(input('Escolha a opção: '))
if menu == 1:
    print('O número {} corresponde a {} em BINÁRIO.'.format(n, bin(n)))
elif menu == 2:
    print('O número {} corresponde a {} em OCTAL.'.format(n, oct(n)))
elif menu == 3:
    print('O número {} corresponde a {} em HEXADECIMAL'.format(n, hex(n)))
else:
    print('Opção inválida. Tente novamente.')
