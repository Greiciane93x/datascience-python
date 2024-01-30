# cerquilha indica o início de um comentário. O Python ignora esses comentários, mas eles orientam
# os leitores do código.

for i in [1, 2, 3, 4, 5]:
    print(i)                # primeiro linha do bloco "for i"
    for j in [1, 2, 3, 4, 5]:
        print(j)            # primeira linha do bloco "for j"
        print(i + j)        # última linha do bloco "for j"
    print(i)                # última linha do bloco "for i"
print("done looping")


long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# para facilitar a leitura do código:

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

# também é possível usar uma barra invertida para indicar que a instrução continua na próxima linha, mas isso raramente ocorre:
two_plus_three = 2 + \
                 3

# A formatacão de espaço em branco pode dificultar as ações de copiar e colar o código no shell do Python. Por exemplo, se você
# tentasse colar o seguinte código no shell comum do Python:

for i in [1, 2, 3, 4, 5]:
    # Observe a linha em branco
    print(i)

# Apareceria a seguinte reclamação: IdentationError: expected an indented block
# Isso ocorre porque o interpretador acha que a linha em branco indica o final do bloco do loop for.
# O IPython tem a função mágica %paste, que copia corretamente o conteúdo da área de transferência, com os espaçosem branco e
# tudo mais. Só isso já é um excelente motivo para usar o IPython.

