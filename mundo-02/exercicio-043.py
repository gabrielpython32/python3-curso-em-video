# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
# status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso;
# Entre 18.5 e 25: peso ideal;
# de 25 até 30: sobrepeso;
# de 30 até 40: obesidade;
# acima de 40: obesidade mórbida.
peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc == 18.5 or imc < 25:
    print('Você está no peso ideal.')
elif imc == 25 or imc < 30:
    print('Você está com sobrepeso.')
elif imc == 30 or imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
