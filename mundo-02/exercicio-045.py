'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
from random import randint
reiniciar = str('s')
while reiniciar == 's':
    print('-=' * 20)
    print('Pedra, papel e tesoura.')
    print('-=' * 20)
    print('''Selecione uma opção:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO-')
    sleep(0.7)
    print('KEN-')
    sleep(0.7)
    print('PO!!!')
    sleep(0.4)
    computador = randint(0, 2)
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    print('-=' * 20)
    print('O computador jogou: {}'.format(opcoes[computador]))
    print('O jogador jogou: {}'.format(opcoes[jogador]))
    print('-=' * 20)
    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:  # jogador jogou PEDRA
            print('RESULTADO: EMPATE!')
        elif jogador == 1:  # jogador jogou PAPEL
            print('RESULTADO: JOGADOR VENCE!')
        elif jogador == 2:  # jogador jogou TESOURA
            print('RESULTADO: JOGADOR PERDE!')
    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:  # jogador jogou PEDRA
            print('RESULTADO: JOGADOR PERDE!')
        elif jogador == 1:  # jogador jogou PAPEL
            print('RESULTADO: EMPATE!')
        elif jogador == 2:  # jogador jogou TESOURA
            print('RESULTADO: JOGADOR VENCE!')
    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:  # jogador jogou PEDRA
            print('RESULTADO: JOGADOR VENCE!')
        elif jogador == 1:  # jogador jogou PAPEL
            print('RESULTADO: JOGADOR PERDE!')
        elif jogador == 2:  # jogador jogou TESOURA
            print('RESULTADO: EMPATE!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.')
    print('-=' * 20)
    reiniciar = str(input('Deseja jogar novamente? [S/N]'))
    print('\n' * 50)
