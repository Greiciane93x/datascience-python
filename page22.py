"""Quando algo dá errado, o Python gera uma exceção. Se não forem tratadas,
as exceções causarão falhas no programa. Para tratá-las, você pode usar try e except"""

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")


"""Apesar de terem uma má reputação em muitas linguagens, no Python, as exceções são
utilizadas sem grilo para deixar o código mais limpo; de vez em quando, faremos isso."""

