# Exercício 1: Contagem de Vogais
# Escreva um programa que peça ao usuário para inserir uma string e
# em seguida, conte o número de vogais (a, e, i, o, u) nessa string.

# qt_vogal_a = 0
# qt_vogal_e = 0
# qt_vogal_i = 0
# qt_vogal_o = 0
# qt_vogal_u = 0

# st_usuario = input('Insura uma frase para que possamos contar as vogais! \n').lower()

# for i in range(0,len(st_usuario)):
#     if st_usuario[i] == 'a': qt_vogal_a += 1
#     elif st_usuario[i] == 'e': qt_vogal_e += 1
#     elif st_usuario[i] == 'i': qt_vogal_i += 1
#     elif st_usuario[i] == 'o': qt_vogal_o += 1
#     elif st_usuario[i] == 'u': qt_vogal_u += 1
    
# print(f"A quantidade de vogais inseridas foram: \n Vogais A: {qt_vogal_a} \n Vogais E: {qt_vogal_e} \n Vogais I: {qt_vogal_i} \n Vogais O: {qt_vogal_o} \n Vogais U: {qt_vogal_u}")


list_vogais = ['a','e','i','o','u']
st_usuario = input('Insura uma frase para que possamos contar as vogais! \n').lower()
qt_vogais = 0
 
for i in st_usuario:
    if i in list_vogais:
        qt_vogais += 1

print(qt_vogais)