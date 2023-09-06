# Exercício 5: Substituição de Substring
# Peça ao usuário para inserir uma string e, em seguida, 
# substitua todas as ocorrências de uma substring específica por outra substring. 
# Por exemplo, substitua todas as ocorrências de "gato" por "cachorro".

frase = input('Insira uma frase: ')
palavra = input('Insira uma palavra que queira substituir na frase acima: ')
ch_palavra = input(f'Insira qual palavra deve substituir a palavra {palavra}: ')

frase_changed = frase.replace(palavra, ch_palavra)

print(f'A sua frase ficou assim: \n\n "{frase_changed.capitalize()}"\n')