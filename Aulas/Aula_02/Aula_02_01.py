# Operadores de atribuição 
#  +=, -=,  *=

# teste = 20
# teste += 10
# print (teste)


"""
para adicionar valores em listas
teste: list = []
teste.append(20)


teste: list = []
teste.append(20)
teste.append(30)
print(teste)
""" 


# estrutura condicional (if, elif, else)

# if not(True):
#     print('verdadeiro')
# elif 'teste' == 'teste':
#     print('teste')
# else:
#     print('else')

# Loop while
# teste = False
# contador = 10
# while not (contador <= 10):
#     print(contador)
#     contador -= 1

# Loop for
# lista: list =[0,1,2,3]
# for n in lista:
#     print (n)

# desempacotamento de dados de uma lista num for 
# lista = [('nome', 'Xean'),('idade','23'),('profissao','garoto de programa')]
# for n, valor in lista:
#     print(n,valor)

# Loop com continue e break
# lista = ['Xean','Xamile','Xoão','Xonatan']
# for nome in lista:
#     if (nome == 'Xoão'):
#         break
#     else:
#         print(nome)
#         continue

# Loop com função range()
for x in range(0,10): #primeiro parâmetro é o start e o segundo parâmetro o stop
    print(x)

# Função range
# Função enumerate()
# lista = ['valor1', 'valor2', 'valor3']
# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     print(lista[item[0]])

# for index, valor in enumerate(lista):
#     print(lista[index])

# Função endrange do múdulo random
# import random 
# valor = random.randrange(0,11)

# print(valor)