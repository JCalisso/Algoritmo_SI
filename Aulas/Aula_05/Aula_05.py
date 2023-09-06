

# Acessar determinado caracater
# Podemos acessar caracteres individuais em uma string usando um índice


# fatiando strings
# Podemos fatiar uma string para obter uma parte específica da string
# especificando um intervalo de índices

# email = 'faccat@faccat.com'
# dominio_email = email[6:len(email)]

# print (email, dominio_email

# para reverter uma string em

# exemplo = 'exemplo'
# exemplo_revertido = exemplo[::-1] # :: igual um passo a passo de um slice, o -1 reverte a string 

# print (exemplo, exemplo_revertido)


# comprimento de uma string

# teste = 'teste'
# print (len(teste)) # len é usado para pegar o tamanh 

# string1 = 'olha, '
# string2 = 'mundo'

# string_real = string1 + string2 # primeira forma 
# string_real = ''.join([string1,string2]) # JOIN precisa de uma lista (iterável) ''.join(['',''])

# print (string_real)

# funcoes em strings
# exemplo = ' eXemplo de uso'

# print(exemplo.lower()) # deixa tudo minusculo
# print(exemplo.upper()) # deixa tudo maisculo
# print(exemplo.capitalize()) # deixa a primeira letra maiúscula
# print(exemplo.title()) # deixa todas as primeiras letras maiúsculas

# print(exemplo.strip('') )

# Substituicao
exemplo = 'O mundo está girando'
novo_exemplo = exemplo.replace('mundo', 'planeta')

print(exemplo)
print(novo_exemplo)