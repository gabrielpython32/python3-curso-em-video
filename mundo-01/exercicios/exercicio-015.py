dias = int(input('Quantos dias o carro esteve alugado? '))
km = float(input('Quantos kilômetros o carro percorreu? '))
calc = (60 * dias) + (km * 0.15)
print('O valor do aluguel é R${:.2f}'.format(calc))
