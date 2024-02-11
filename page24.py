"""As tuplas são muito parecidas com as listas, mas não podem ser modificadas.
Com uma tupla, podemos fazer quase tudo que se pode fazer com uma lista, menos modificá-la.
Para especificar uma tupla, use parênteses (ou nada) em vez de colchetes.
"""

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

print(f'my_list: {my_list}')

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

"""As tuplas são uma forma eficaz de usar funções para retornar múltiplos valores"""


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

print(f'soma: {s}\n'
      f'produto: {p}')

""" As tuplas (e as listas) também podem ser usadas em atribuições múltiplas"""

x, y = 1, 2
x, y = y, x

print(f'x: {x}')
print(f'y: {y}')
