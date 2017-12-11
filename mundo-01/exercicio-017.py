co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vale {:.2f}'.format(hip))

# método 02 abaixo:
# from math import hypot
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hip = hypot(co, ca)
# print('A hipotenusa vale {:.2f}'.format(hip))
