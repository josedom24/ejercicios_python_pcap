class SuperUno:
    pass


class SuperDos:
    pass


class Sub(SuperUno, SuperDos):
    pass


def printBases(clase):
    print('( ', end='')

    for x in clase.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)

