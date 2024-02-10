"""Provavelmente, a estrutura de dadds mais fundamental do Python é a lista. Uma lista é apenas uma coleção ordenada
(parecida com o array das outras linguagens, mas com funcionalidades adicionais)"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)
list_sum = sum(integer_list)

print(
    f'integer_list: {integer_list}, heterogeneous_list: {heterogeneous_list}, list_length: {list_length}, list_sum: {list_sum}')

"""Você pode obter e definir o elemento de número n de uma lista usando colchetes: """

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

print(f'zero: {zero}')  # igual a 0, as listas são indexadas a partir do 0
print(f'one: {one}')  # igual a 1
print(f'nine: {nine}')  # igual a 9, 'Pythonic' para o último elemento
print(f'eight: {eight}')  # igual a 8, 'Pythonic' para o último elemento
print(f'x[0]: {x[0]}')  # agora x é [-1,1,2,3, ..., 9]

