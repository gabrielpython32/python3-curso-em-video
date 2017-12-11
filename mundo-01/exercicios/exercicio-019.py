a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
import random
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O aluno escolhido foi {}.'.format(sorteio))
