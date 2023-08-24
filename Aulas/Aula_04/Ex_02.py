# Exercicio 2
# Inicialize uma lista vazia. Permita que o
# usuário adicione nomes de animais a essa lista até que ele insira "sair". 
# Em seguida, remova o último elemento da lista e exiba a lista final.

animals_list = []

continue_list = ('continuar','sair')  # continuar | sair

while continue_list != 'continuar':
    # animals_list = print('Insira o nome de bicho: ')
    sn_continua = str(input('Deseja continuar? insira "continuar", ou "sair": '))

    if sn_continua in continue_list[1]:
        print('término do programa')
        break
    else:
        continue