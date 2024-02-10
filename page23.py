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
