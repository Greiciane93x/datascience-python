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