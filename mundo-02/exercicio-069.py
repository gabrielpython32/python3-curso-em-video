'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados
C) Quantas mulheres com menos de 20 anos.
'''

print('''*********************************
* Verificador de Idades e Sexos *
*********************************''')

continuar = 's'
pessoasmais18 = homens = mulhermenos20 = 0

while continuar == 's':

    idade = input('Digite a idade: [Ex: 24]')

    while idade.isnumeric() is False:
        print(f'''Você digitou '{idade}', não é um número inteiro. Tente novamente.''')
        idade = input('Digite a idade: [Ex: 24]')

    sexo = str(input('Digite o sexo: [M/F]')).lower()

    while sexo not in 'mf':
        print(f'''Você digitou '{sexo}', não está entre as opções [M/F].''')
        sexo = str(input('Digite o sexo: [M/F]')).lower()

    if int(idade) > 18:
        pessoasmais18 += 1

    if sexo in 'm':
        homens += 1

    if sexo in 'f' and int(idade) < 20:
        mulhermenos20 += 1

    continuar = str(input('Deseja continuar? [S/N]'))

print(f'\nNo total, tem(os):\n{pessoasmais18} Pessoa(s) maior(es) que 18 anos;\n{homens} Homen(s) cadastrado(s);\n{mulhermenos20} Mulher(es) com menos de 20 anos.')
