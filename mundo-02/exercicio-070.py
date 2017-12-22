'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato.
'''

print('''*********************
* Mercadinho Maroto *
*********************''')

continuar = 's'
produtobarato = ''
total = mais1000 = maisbarato = cont = 0

while continuar == 's':
    produto = str(input(f'Digite o nome do {cont + 1}° produto: '))
    preco = float(input(f'Digite o preço do {produto} [R$]: '))
    continuar = str(input('Deseja continuar? [S/N]')).lower()

    total += preco

    if preco > 1000:
        mais1000 += 1

    # Demorei aproximadamente 01 hora para solucionar o problema do menor preço.
    # Sim, fiquei um pouco estressado, pesquisei muito também! :D
    if cont == 0:
        maisbarato = preco
        produtobarato = produto

    else:

        if preco < maisbarato:
            maisbarato = preco
            produtobarato = produto

    cont += 1

print(f'''
No total:
R${total} gasto(s) na compra.
{mais1000} produto(s) que custa(m) mais de R$1.000,00.
{produtobarato} é o produto mais barato da compra, que custou R${maisbarato}.''')
