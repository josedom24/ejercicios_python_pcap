def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")