# Exercício 3 - Loop for utilizando a função range:
# Crie um programa que exiba a tabuada de multiplicação de um número fornecido pelo usuário. 
# O programa deve exibir a tabuada de 1 a 10.

number = int(input('Insira o número da tabuada que deseja descobrir: '))
for i in range(0,11):
    print(f'{i} x {number} = {i * number}')    
