try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print (y)
except (ValueError, ZeroDivisionError):
    print("Error: Por valor incorrecto o por división por 0")
print("FIN")