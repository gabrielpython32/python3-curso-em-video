'''
Melhore o jogo do EXERCÍCIO 028 (Mundo 01) onde o computador vai 'pensar' em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''

from random import randint

print('''****************************
* Jogo da adivinhação v2.0 *
****************************''')

tentativa = 0
computador = randint(1, 11)

jogador = int(input('Escolha um número de 0 a 10: '))

while jogador != computador:
    tentativa += 1

    if jogador < computador:
        jogador = int(input('Tente um número maior: '))

    elif jogador > computador:
        jogador = int(input('Tente um número menor: '))

if jogador == computador:
    tentativa += 1
    print('Você acertou! E foi na {}ª tentativa!'.format(tentativa))
