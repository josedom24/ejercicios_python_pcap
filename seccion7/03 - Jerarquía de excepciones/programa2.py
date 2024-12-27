try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema Aritmético!")

print("FIN.")


try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema Aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")

print("FIN.")

