# Exercicio 2 - Loop For
# Crie um programa que peça ao usuario alguns items de compra em seguida exiba a lista


itens_pedido = []
itens = 0
for itens in range(0,3):
    item = input(f"Informe o item de número {itens}: ")
    itens_pedido.append(item)

for itens in itens_pedido:
    print(itens)

# Toda lista é iteravel, ela só percorre os index de uma lista