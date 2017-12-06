# A confederação Nacional de Natação precisa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo
# com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER
from datetime import date
atual = date.today().year
n = int(input('Digite a idade do atleta: '))
cat = atual - n
if cat <= 9:
    print('A classificação do atleta é MIRIM.')
elif cat <= 14:
    print('A classificação do atleta é INFANTIL.')
elif cat <= 19:
    print('A classificação do atleta é JUNIOR.')
elif cat <= 25:
    print('A classificação do atleta é SÊNIOR.')
elif cat > 25:
    print('A classificação do atleta é MASTER.')
print('Pois ele(a) tem {} anos.'.format(cat))
