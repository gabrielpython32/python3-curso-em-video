'''Refaça o exercício 09, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço 'for'.'''
contador = 0
print('-=' * 5, 'Tabuada', '-=' * 5)
num = int(input('\nDigite um número para verificar sua tabuada:'))
print('\nA tabuada de \033[4;32;0m{}\033[0;0m é:\n'.format(num))
for contador in range(-1, 10):
    contador += 1
    res = num * contador
    print('{} X {} = {}'.format(num, contador, res))
print('\n=== FIM ===')
