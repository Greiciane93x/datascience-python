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

print(f'dd_pair = {dd_pair}')

"""Isso será útil quando usarmos dicionário para coletar os resultados de alguma chave sem verificar se ela existe a 
cada operação"""

# Contadores
"""O Counter (contador) converte uma sequência de valores em algo parecido com objetivo defaultdict(int) mapenado
as chaves correspondentes às contagens: """

from collections import Counter

c = Counter([0, 1, 2, 0])
print(f'c: {c}')

"""Essa é uma forma bem simples de resolver o problema do word_counts: """

word_counts = Counter(document)

"""Uma instância Counter contém um método most_common bastante útil: """

for word, count in word_counts.most_common(10):
    print(word, count)

