"""Outra estrutura fundamental é o dicionário, que associa valores a chaves e permite a rápida
recuperação do valor correspondente a uma determinada chave: """

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

print(f'Pythonic: {empty_dict}\n',
      f'menos Pythonic: {empty_dict2}\n'
      f'dicionário literal: {grades}')

"""Para pesquisar o valor de uma chave, vcê pode usar os colchetes: """
joels_grade = grades["Joel"]

print(f'joels_grade: {joels_grade}')

"""Mas parecerá um KeyError se você procurar uma chave que não está dicionário: """

try:
    kates_grade = grades["Kates"]
except KeyError:
    print("no grade for Kate!")

"""Para verificar a existência de uma chave, você pode usar o in: """
joel_has_grade = grades.get("Joel", 0)
print(f'joel_has_grade: {joel_has_grade}')

kates_grade = grades.get("Kate", 0)
print(f'kates_grade: {kates_grade}')

no_one_grade = grades.get("no One")
print(f'no_one_grade: {no_one_grade}')

"""Você também pode atribuir pares de valor-chave usando os colchetes"""
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

print(f'grades: {grades}')

"""Como vimos no Capítulo 1, os dicionários podem representar dados estruturados: """

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "science", "#datascience", "#awesome", "#yolo"]
}

print(f'tweet: ${tweet}')
