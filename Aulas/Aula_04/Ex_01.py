# Exercicio 1
# Crie uma lista com alguns nomes de frutas.
# Peça do usuário para digitar um número de 1 a
# N (onde N é o número de frutas na lista) e, em seguida, exiba a fruta correspondente a esse número na lista.

fruit_list = ['banana', 'uva', 'maçã','morango','maracujá', 'pessego', 'pitaia']

qt_fruits = len(fruit_list)

selected_fruit = int(input(f"Insira um número (inteiro) entre 1 e {qt_fruits}: "))

selected_fruit -= 1

if (selected_fruit > qt_fruits) or (selected_fruit < qt_fruits)  :
    print(f'A fruta selecionada é: {fruit_list[selected_fruit]}')
else:
    print('Fruta selecionada não registrada ')

