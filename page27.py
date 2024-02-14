"""O defaultdict diciona um valor para ela usando a função de argumento zero que indicamos ao criá-lo.
Para usar os defaultdicts, você deve importá-los das collections: """
from collections import defaultdict

document = "text"
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

"""Esses recursos também são uteis com list, dict e outras funções: """
dd_list = defaultdict(list)
dd_list[2].append(1)

print(f'dd_list = {dd_list}')

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

print(f'dd_dict = {dd_dict}')

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1


"""Isso será útil quando usarmos dicionário para coletar os resultados de alguma chave sem verificar se ela existe a 
cada operação"""
