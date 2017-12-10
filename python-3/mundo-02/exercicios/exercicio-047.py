'''Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.'''

print('Mostrando todos os números pares no intervalo de 1 a 50:')

'''método 01 - mais pesado no processamento:
for num in range(1, 51):
    if num % 2 == 0:
        print(num)
print('=== FIM ===')'''

# método 02 - mais leve no processamento (recomendado usar):
for num in range(2, 51, 2):
    print(num)
print('=== FIM ===')
