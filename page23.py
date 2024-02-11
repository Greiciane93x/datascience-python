"""Você também pode usar os colchetes para fatiar as listas. A fatia i:j contém
todos os elementos de i (incluído) a j (não incluído). Se o início da fatia não for indicado ela
 começará no início da lista; se o final da fatia não for indicado, ela terminará no final da lista"""

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

print(f'first_three: {first_three}\n'
      f'three_to_end: {three_to_end}\n'
      f'one_to_four: {one_to_four}\n'
      f'last_three: {last_three}\n'
      f'without_first_and_last: {without_first_and_last}\n'
      f'copy_of_x: {copy_of_x}\n'
      )

"""Do mesmo modo, você pode fatiar strings e outros tipos de sequências
A fatia pode receber um terceiro argumento para indicar seu stride, que pode ser negativo 
"""

every_third = x[::3]
five_to_three = x[5:2:-1]

print(f'every_third: {every_third}\n')
print(f'five_to_three: {every_third}\n')

"""O Python dispõe de um operador in para verificar a associação à lista"""

a1 = 1 in [1, 2, 3]
a2 = 0 in [1, 2, 3]

print(f'{a1}\n'
      f'{a2}')

"""Como essa verificação analisa todos os elementos da lista, você só deve executá-la se a lista for bem pequena
(ou se o tempo da verificação não for importante)"""
"""É fácil concatenar lista. Para modificar a lista, você pode usar extend e adicionar itens de outra coleção:"""

x = [1, 2, 3]
x.extend([4, 5, 6])

print(f'approach 1: {x}')

"""Se não quiser modificar x, você pode usar a adição de listas"""
x = [1, 2, 3]
y = x + [4, 5, 6]

print(f'approach 2: {y}')
