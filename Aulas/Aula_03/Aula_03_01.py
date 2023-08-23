"""
Modularização

Funções - fora do escopo de uma classe (tudo em python é uma classe)
embutido em uma classe se tem MÉTODOS
quando não se fala de Classes, fala-se de função 
""" 
from module import soma, teste
# import module

num_1 = int(input("informe o primeiro número: "))
num_2 = int(input("informe o segundo número: "))

result_sum = soma(num_1, num_2)

print(result_sum)
    