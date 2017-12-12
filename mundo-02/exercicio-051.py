'''
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
'''
primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + 10 * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')
