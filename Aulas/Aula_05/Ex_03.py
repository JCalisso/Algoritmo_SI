# Exercício 3: Palíndromo
# Peça ao usuário para inserir uma palavra e determine se é um palíndromo 
# (uma palavra que é a mesma se lida de trás para frente, como "radar" ou "level").

string_usuario = input('Insura uma palavra e descubra se ela é um palíndromo: \n')
string_reversed = string_usuario[::-1]

if string_usuario == string_reversed:
    print('Sua palavra é um palíndromo!\n')
else:
    print('Sua palavra não é um palíndromo...\n')