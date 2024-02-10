def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)


my_double = 10
x = apply_to_one(my_double)

# Também é fácil criar pequenas funções anônimas, as lambdas:
y = apply_to_one(lambda z: x + 4)


# Também é possível atribuir lambdas a variáveis, embora o recomendado é utilizar o def:
# another_double = lambda x: 2 * x # não faça isso

def another_double(v):
    """Faça isso"""
    return 2 * v


# Os parâmetros da função tambpem podem receber argumentos padrão, que devem ser especificados se você quiser
# obter um valor diferente do padrão :

def my_print(message="my default message"):
    print(message)

    my_print("Helo")
    my_print()


# Às vezes, é útil especificar argumentos pelo nome:

def full_name(first="What's his name?", last="Something"):
    return first + " " + last


full_name("Joe,l", "Grus")  # "Joel Grus"
full_name("Joel")                    # "Joel"
full_name(last="Grus")               # "What's-his-name Grus"
