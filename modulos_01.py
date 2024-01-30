# Alguns recursos do Python não são carregados por padrão, como certos componentes integrados à linguagem e elementos
# externos, disponiveis para download. Para usar esses recuros, você terá que import (importar) seus respectivos módulos
# Uma opção é importar o módulo em questão:
import re
my_regex = re.compile("[0-9]+", re.I)

# Aqui, re é o módulo que contém as funções e constantes aplicáveis às expressões regurales. Após esse tipo de import,
# para acessar as respectivas funções, você deve usar o prefixo re...
# Se já houve outro re no código, você pode usar um alias:
# import re as regex
# my_regex = regex.compile("[0-9]+", regex.I)