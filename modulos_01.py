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
# Você pode fazer isso se o módulo tiver um nome complicado ou se precisar digitar um trecho muito longo. Por exemplo,
# para visualizar dados com o matplotlib, existe um padrão:


#import matplotlib as plt
# plt.plot(... )

#Para obter valores específicos de um módulo, você pode importá-los expressamente e usá-los sem qualificação:

# from collections import defaultdict, Counter
# lookup = defaultdict(int)
# my_counter = Counter()

# Para fazer uma bagunça, você pode importar o conteúdo inteiro de um módulo para o namespace, substituindo (sem querer)as variáveis definidas
# anteriormente :

# match = 10
# from re import *  # opa o re tem uma função match
# print(match)      # "<function match at 0x10281e6a8>"
# Mas, como você não é bagunceiro, nunca faça isso
