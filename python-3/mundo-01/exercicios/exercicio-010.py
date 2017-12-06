reais = float(input('Digite quanto dinheiro, em reais, que você tem na carteira: '))
cotacao = float(input('Digite quanto está a cotação da moeda desejada para fazer o cálculo: '))
calculo = reais / cotacao
print('Com R${} você pode comprar {:.2f} na moeda convertida.'.format(reais, calculo))
