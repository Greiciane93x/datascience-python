"""Além de procurar por chaves específicas, podemos conferir todas elas"""

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print(f'Tweet keys: {tweet_keys}')
print(f'Tweet values: {tweet_values}')
print(f'Tweet items: {tweet_items}')

var1 = "user" in tweet_keys
var2 = "user" in tweet
var3 = "joelgrus" in tweet_keys

print(f'Verdadeiro, mas nao Pythonic: {var1}')
print(f'forma Pythonic de verificar as chaves: {var2}')
print(f'Verdadeiro (lento, mas unica forma de verificar): {var3}')

"""As chaves do dicionário devem ser hashtable [com função hashm imutáveis], logo as listas 
não podem ser usadas como chave, se você precisar de uma chave com várias partes, use uma tupla ou transforme a chave 
a chave em uma string"""

# defaultdict
"""Imagine que você deseja contar as palavras de um documento. Uma abordagem óbvia seria criar um dicionário com 
chaves para palavras e valores para a contagem. Ao verificar cada palavra, você pode incrementar a contagem (se ela
já estiver no dicionario) ou  adicioná-la ao dicionário (se ela ainda não estiver nele): """

document = "text"

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

"""Você também pode usar o método **é melhor pedir perdão do que permissão**, tratando a exceção gerada na pesquisa pela 
chave ausente"""

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

"""Uma terceira abordagem é usar o get, que lida de forma muito interesante com chaves ausentes:"""
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

"""Mas, como esses métodos são um tanto quanto complicados, o defaultdict é um bom recurso. Embora pareça um dicionário
comum, quando procuramos uma chave que está contida nele. """
