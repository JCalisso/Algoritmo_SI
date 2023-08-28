# Exercicio 2
# Inicialize uma lista vazia. Permita que o
# usuário adicione nomes de animais a essa lista até que ele insira "sair". 
# Em seguida, remova o último elemento da lista e exiba a lista final.

def set_animals():
    animal = input('Insira o nome de bicho: ')
    animals_list.append(animal)

animals_list = []

continue_list = ('continuar','sair')  # continuar | sair
sn_continua = continue_list[0]

while sn_continua == 'continuar': 
    set_animals()
    sn_continua = str(input('Deseja continuar? insira "continuar", ou "sair": '))

    if sn_continua in continue_list[1]:
        print('Término do programa. Os animais selecionados foram: ')
        print(animals_list)
        break
    else:
        continue