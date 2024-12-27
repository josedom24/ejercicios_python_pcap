def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")
