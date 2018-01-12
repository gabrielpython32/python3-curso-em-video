
apenas com o while true no inicio, flw.


c10 = c20 = c50 = c1 = 0
while True:
    print('{:-^40}'.format('CAIXA ELETRÔNICO'))
    valor_sacado = int(input('Digite o valor que você deseja sacar [valor inteiro]: R$'))
    while valor_sacado is not 0:
        if valor_sacado >= 50:
            c50 += 1
            valor_sacado -= 50
        elif valor_sacado >= 20:
            c20 += 1
            valor_sacado -= 20
        elif valor_sacado >= 10:
            c10 += 1
            valor_sacado -= 10
        elif valor_sacado < 10:
            c1 += 1
            valor_sacado -= 1
    if valor_sacado == 0:
        break
print('{:-^40}'.format('NOTAS A SEREM SACADAS'))
print(f'{c1} notas de R$1')
print(f'{c10} notas de R$10')
print(f'{c20} notas de R$20')
print(f'{c50} notas de R$50')
print('obrigado por usar o servido ')
