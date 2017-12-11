velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você vai pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
