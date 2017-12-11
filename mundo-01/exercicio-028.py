from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual é...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei em {} e não no {}'.format(computador, jogador))
