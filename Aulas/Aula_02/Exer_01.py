# Exercício 1 - Estrutura condicional (if, elif, else):
# Escreva um programa que receba a idade de uma pessoa e informe 
# se ela é criança (menor de 12 anos), #adolescente (entre 12 e 17 anos)
# ou adulta (18 anos ou mais).


age = int(input('Insira sua idade: '))

if age <= 12:
    print('vc é uma criança')
elif age > 12 and age <= 17:
    print('vc é um adolescente chato')
else:
    print('vc é adulto e tem que pagar imposto de renda')   

print('')