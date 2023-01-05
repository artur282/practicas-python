# generadores
def comesticos():

    num = 0
    while True:
        yield num
        num += 1


def perfumes():

    num = 0
    while True:
        yield num
        num += 1


def farmarcia():

    num = 0
    while True:
        yield num
        num += 1

# decoradores


def decorador(funcion):
    print(f'has tomado un turno ')
    funcion()
    print('por favor espera')






