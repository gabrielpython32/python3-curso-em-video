'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

print('Mostrando números ímpares, múltiplos de 3, de 1 até 500:')
soma = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        print(num)  # preferi não usar o [end=''] para o print poder ser mostrado na vertical
        soma = soma + num  # pode ser colocado também: [soma += num]
        contador = contador + 1  # pode ser colocado também: [contador += 1]
print('A soma de todos os valores é {} e foram somados {} vezes.'.format(soma, contador))
