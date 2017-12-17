'''
Faça um programa que leio o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
print('''**************************************
* Verificador: Feminino ou Masculino *
**************************************''')
sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite novamente: [M/F] ')).strip().upper()
print('Sexo {} registrado.'.format(sexo))
