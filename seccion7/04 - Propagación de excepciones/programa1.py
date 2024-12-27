def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema Aritmético!")
        return None

bad_fun(0)
print("FIN.")