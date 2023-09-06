# Exercício 2: Reversão de String
# Peça ao usuário para inserir uma string e, em seguida, imprima a string de trás para frente.

string_user = input('Insira uma palavra para que ela seja invertida! \n')
string_reversed = string_user[::-1]

print(f'A sua palavra: "{string_user.upper()}", quando invertida fica: "{string_reversed.upper()}".')