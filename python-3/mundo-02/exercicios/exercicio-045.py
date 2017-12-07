'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
from random import randint
print('''Selecione uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
computador = randint(0, 2)
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
print('-=' * 15)
print('O computador jogou: {}'.format(opcoes[computador]))
print('O jogador jogou: {}'.format(opcoes[jogador]))
print('-=' * 15)
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
print('-=' * 15)
