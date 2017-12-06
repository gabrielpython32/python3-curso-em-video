# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.
casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do salário: '))
anos = float(input('Quantos anos de financiamento? '))
pres = casa / (anos * 12)
min = sal * 30/100
if pres <= min:
    print('Empréstimo APROVADO! A prestação será de R${:.2f}'.format(pres))
else:
    print('Empréstimo NEGADO! A prestação será de R${:.2f} e ultrapassou o limite de 30% do salário.'.format(pres), end='')
    print('Para estar dentro do limite, a prestação deveria ser de R${}'.format(min))
print('Tenha um bom dia!')
