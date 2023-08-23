# Exercício 1 - Estrutura condicional (if, elif, else):
# Escreva um programa que receba a idade de uma pessoa e informe 
# se ela é criança (menor de 12 anos), #adolescente (entre 12 e 17 anos)
# ou adulta (18 anos ou mais).

def validate_age(age: int):
    if (age <= 12):
        return "criança"
    elif(age > 12 and age <= 17):
        return "adolescente"
    else:
        return "adulto"

age = int(input('Insira sua idade: '))

print(f"Segundo a sua idade {age}, você é um(a) {validate_age(age)}")