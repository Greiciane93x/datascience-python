# String (Cadeias de Caracteres)
# As strings podem ser delimitadas por aspas simples ou duplas (mas sempre combinando):

single_quoted_string = 'data science'
double_quoted_string = "data science"

# No Python, a barra invertida serve para codificar caracteres especiais. Ex:
tab_string = "\t"  # representa  o caractere tab
len(tab_string)  # é 1

"""Para usar o caractere da barra invertida (como vemos nos nomes dos diretórios e nas expressões regulares do
Windows), voce podde criar strings brutas com r """

not_tab_string = r"\t"  # representa os caracteres `\` e `t`
len(not_tab_string)  # é 2

# Para criar strings de várias linhas, use três aspas duplas:
muilti_line_string = """Esta é a primeira linha, 
e esta é a segunda linha 
e esta é a terceira linha"""

# No Python 3.6, já um novo recurso: a f-string, uma forma simples de substituir
# os valores nas strings. Por exemplo, quando o nome e o sobrenome são indicados separadamente:

first_name = "Joel"
last_name = "Grus"

"""Nesse caso, queremos formar o nome completo com eles. Há várias formas de construir uma string full_name: """
full_name = f"{first_name} {last_name}"


# Utilizaremos esse método ao longo do livro


