# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista (dinheiro ou cheque): 10% de desconto;
# À vista (cartão de crédito): 5% de desconto;
# Em até 2x no cartão: preço normal;
# Em 3x ou mais no cartão: 20% de juros.
print('=' * 17)
print('Lojinha do Rafael')
print('=' * 17)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA - DINHEIRO/CHEQUE
[ 2 ] À VISTA - CARTÃO DE CRÉDITO
[ 3 ] PARCELADO - 2X NO CARTÃO DE CRÉDITO
[ 4 ] PARCELADO - 3X OU MAIS NO CARTÃO DE CRÉDITO''')
opcao = int(input('Qual é a opção desejada? '))
if opcao == 1:
    calc = preco - (preco * 10/100)
    print('Pagamento: dinheiro/cheque. Sua compra de {} vai custar {} no total.'.format(preco, calc))
elif opcao == 2:
    calc = preco - (preco * 5/100)
    print('Pagamento: CARTÃO DE CRÉDITO. Sua compra de {} vai custar {} no total.'.format(preco, calc))
elif opcao == 3:
    calc = preco
    parcela = preco / 2
    print('Pagamento: 2X NO CARTÃO DE CRÉDITO SEM JUROS. Sua compra de {} vai custar {} no total.'.format(preco, preco))
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    calc = preco + (preco * 20/100)
    qtdeparcelas = int(input('Em quantas parcelas deseja pagar? '))
    valparcelas = calc / qtdeparcelas
    print('Pagamento: {}X NO CARTÃO DE CRÉDITO COM JUROS. Sua compra de {} vai custar {} no total.'.format(qtdeparcelas, preco, calc))
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(qtdeparcelas, valparcelas))
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')
