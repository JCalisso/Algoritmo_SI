# Exercicio 2 - Loop For
# Crie um programa que peça ao usuario alguns items de compra em seguida exiba a lista

# GAMBIARRA FUNCIONAL
lista = ['vazio']
for item in lista:
    sn_insere_item = int(input('Deseja inserir itens na lista? [1] - Sim | [0] - Não \n' ))
    if (sn_insere_item < 0 or sn_insere_item > 1):
        print('Opção indisponível.')
        break
    elif sn_insere_item == 1:
        lista.append(input('Insira seu item na lista de compras: \n'))
        continue
    else:
        lista.remove('vazio')
        print('Sua lista de compras é:')
        print(lista)
        break

        