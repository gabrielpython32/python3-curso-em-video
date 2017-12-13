'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres têm menos de 20 anos.
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
nomemulher = ''
listamulher = []
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':  # in 'Mm': para M ou m quando for digitado.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        listamulher.append(nome)
mediaidade = somaidade / 4
print('\nA média de idade do grupo é de {} anos.'.format(mediaidade))
if nomevelho == '':
    print('Não há ninguém do sexo masculino.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
if totmulher20 == 0:
    print('Não há ninguem abaixo dos 20 anos do sexo feminino.')
elif totmulher20 == 1:
    print('Ao todo só há uma mulher abaixo dos 20 anos e seu nome é {}.'.format(nomemulher))
else:
    listamulher.append(nome)
    print('Ao todo são {} mulheres e seus nomes são {}'.format(totmulher20, listamulher))
