
# Exercício 4 - Loop while com continue e break: 
# Faça um programa que informe se o valor da compra 
# dos items Ovos, Leite, Café e Arroz 
# atingiram o limite de 20 reais disponiveis na conta.

def show_product_list(GONDULA):
    for idx, item in enumerate(GONDULA):
        print(f"{idx} - {item[0]}: {item[1]}")

def validate_wallet(total: float, wallet: float):
    if total >= wallet:
        print("Voce ja atingiu o limite da carteira.")
        return False
    else:
        return True
        
def increment_order():
    result = 0.0

    item = int(input("Digite o numero do item que deseja: "))
    valor_item_compra = GONDULA[item][1]
    

    for item_compra in compras_realizadas:
        total += GONDULA[item_compra][1]

    total += valor_item_compra


WALLET = 20.00
GONDULA = [("Eggs", 7.59), ("Milk", 4.99), ("Coffee", 9), ("Rice", 11.10)]

compras_realizadas = []

print("Bem vindos ao mercado Dia a Dia, o que deseja comprar: ")
show_product_list(GONDULA)

item = int(input("Digite o numero do item que deseja: "))
compras_realizadas.append(item)

reorder = int(input("Deseja continuar comprando? 1.SIM 2.NÃO:"))

if reorder == 1:

    continua = True
    while continua:
        show_product_list(GONDULA)
        total = 0
        
        # for item_compra in compras_realizadas:
        #     total += GONDULA[item_compra][1]

        if (validate_wallet(total, WALLET) == False):
            continua = False
            break
        else:
            compras_realizadas.append(item)
            continue

else:
    print("Obrigado pela compra")