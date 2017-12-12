'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
divisores = 0
lista = []
print('''*********************************************
* Verificador de divisores e números primos *
*********************************************\n''')
numero = int(input('Informe um número: '))
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores += 1
        lista.append(divisor)
        print('\033[4m', end=' ')  # sem cor e sublinhado
    else:
        print('\033[0;0m', end=' ')  # sem cor/estilo
    print('{}'.format(divisor), end=' ')
if divisores == 2:
    primo = str('Sim')
else:
    primo = str('Não')
print('''\033[0;0m\n
Legenda: 
[ ___ ] Números divisíveis
[     ] Números não divisíveis''')
print('''\n\033[mNúmero: {}
Primo: {} 
Divisões: {}
Divisores: {}'''.format(numero, primo, divisores, lista))
