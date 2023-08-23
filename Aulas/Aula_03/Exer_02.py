# Exercicio 2 - Loop For
# Crie um programa que peça ao usuario alguns items de compra em seguida exiba a lista

def request_itens(itens: str):

    for itens in range(0,3):
        input_item = input(f"Informe o item de número {itens}")
        itens_bag.append(input_item)


itens = 0
itens_bag = []

for itens in itens_bag:
    print(itens)

# for itens in range(0,3):
#     item = input(f"Informe o item de número {itens}: ")
#     itens_pedido.append(item)

# for itens in itens_bag:
#     print(itens)

# Toda lista é iteravel, ela só percorre os index de uma lista