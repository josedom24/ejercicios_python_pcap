class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("peores noticias")
    else:
        raise ZeroDivisionError("malas noticias")

# Manejo de excepciones con bloques except
for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('División entre cero')

# Manejo de excepciones con bloques except diferenciados
for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('Mi división entre cero')
    except ZeroDivisionError:
        print('División entre cero original')
