# Exercício 4 - Loop while com continue e break: 
# Faça um programa que informe se o valor da compra dos items Ovos, Leite, Café e Arroz 
# atingiram o limite de 20 reais disponiveis na conta.

GONDULA: list = [("Ovos", 7.59), ("Leite", 4.99), ("Café", 9), ("Arroz", 11.10)]

WALLET: float = 20

bag = []
bag_value = 0.0

for i, item in enumerate(GONDULA):
    print(f"{i} - {item[0]} R$ {item[1]}")

item = int(input("Digite o numero do item que deseja: "))
bag.append(item)
bag_value.append(item[1])

keep_buying = int(input("Deseja inserir mais itens? (1) SIM | (2) NÃO"))

if keep_buying == 1:
    continua = True
    while continua:
        for i, item in enumerate(GONDULA):
            print(f"{i} - {item[0]} R$ {item[1]}")

        item = int(input("Digite o numero do item que deseja: "))
        bag.append(item)
        bag_value = GONDULA[item][i]
        total = 0

        for 