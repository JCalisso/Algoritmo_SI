"""
tupla - imutável
lista - mutável

append - insere um valor novo numa lista

pop - utiliza o índice para remover um item da lista, retorna o valor que ele remove
lista.pop(1)

lista.remove(2) - remove da lista sem saber o índice

lista permite mudar o valor
tupla é imutável

performance 
tupla performa melhor por ser fixa (valores imutáveis)

tupla.count() - retorna a quantidade de vezes que um valor se repete numa tupla

tupla = declarada com valores iniciais entre chaves []
lista = declarada com valores iniciais entre parenteses ()

list comprehension

conversão de tupla


"""

# tupla = (1,2,1,3,4,5)
# lista = [1,2,3,4,5,6,5,('teste',2)]

# print(tupla.count(1))
# lista.append('teste 2')
# print (lista)

# lista.pop(2)
# lista.remove(5)
# index = lista.pop(7)

# if 2 in lista:
#     print ('tá na lista')

# lista_de_tupla = list(tupla) # conversão de tupla

# valor = int(input('insira um valor: '))
# resultado = [ variavel_que_recebe for condicoes ] - estrutura basica de uma list comprehension 

# resultado = [x * valor for x in range(1,11)]
# primeiro item - valor que será recuperado
# segundo item - valor que vai percorrer (for)
# terceiro item - validação da condição 
# primeiro percorre o valor, depois valida a condição, se não retorna para o valor que é recuperado
# resultado = [x * valor for x in range(1,11) if x != 3] # é possível adicionar condições
 
tupla = (1,2,1,3,4,5)
print(tupla)

lista_de_tupla = list(tupla)

print (lista_de_tupla)