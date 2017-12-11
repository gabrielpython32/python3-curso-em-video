# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.
a = int(input('Informe o lado 1 do triângulo: '))
b = int(input('informe o lado 2 do triângulo: '))
c = int(input('Informe o lado 3 do triângulo: '))
# Verificando a condição de existência do triângulo:
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Esse triângulo pode existir.')
    # Verificando se o triângulo é equilátero:
    if a == b and a == c and b == a and b == c and c == a and c == b:
        print('Esse triângulo é ÉQUILÁTERO.')
    # Verificando se o triângulo é escaleno:
    elif a != b and a != c and b != a and b != c and c != a and c != b:
        print('Esse triângulo é ESCALENO.')
    # Caso o triangulo nao obedeca a condicao da linha 16:
    else:
        print('Esse triângulo é ISÓSCELES.')
# Caso o triângulo não obedeça a condição da linha 10:
else:
    print('Esse triângulo NÃO pode existir.')
