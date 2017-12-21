'''
Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''

from random import randint

cont = 0

while True:
    computador = randint(0, 11)
    escolha = int(input('''
**********************
* JOGO: PAR OU IMPAR *
**********************

Escolha par ou ímpar: 

[ 1 ] Para PAR
[ 2 ] Para ÍMPAR

Opção: '''))
    jogador = int(input('\nDigite um número: '))
    aposta = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}. No total: {aposta}.', '(PAR)' if aposta % 2 == 0 else '(ÍMPAR)')
    if escolha == 1:
        if aposta % 2 == 0:
            cont += 1
        else:
            print('Você perdeu.')
            break

    if escolha == 2:
        if aposta % 2 != 0:
            cont += 1
        else:
            print('Você perdeu.')
            break

    print(f'Você ganhou, parabéns! No total você tem um total de {cont} vitória(s) consecutiva(s).', '\nJogue novamente...')
print(f'Você teve um total de {cont} vitórias consecutivas.', '\nFIM DE JOGO.')
