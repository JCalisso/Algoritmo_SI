# Exercicio 3
# Crie uma lista com algumas cores. Peça do usuário para digitar o nome de uma cor. 
# Se a cor estiver na lista, permita que o usuário a substitua por outra cor. 
# Caso contrário, adicione a nova cor à tupla.

color_list = ['azul','vermelho','amarelo','roxo','laranja','verde']

color = input('Insira uma cor: \n')
ch_color = ''

if color in color_list:
    sn_ch_color =  input('Cor inserida já cadastrada, deseja substituir? (s | n): \n')
    if sn_ch_color == 's':
        ch_color = input('Insira a nova cor: \n')
        color_list = list(map(lambda index: index.replace(color, ch_color), color_list))
        print(color_list)
else:
    color_list.append(color)