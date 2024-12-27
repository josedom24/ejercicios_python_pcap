try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print (y)
except:
    print("Oh cielos, algo salió mal...")


try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print (y)
except ValueError:
    print("Error: Datos no válidos, ingresa un número entero.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
except:
    print("Oh cielos, algo salió mal...")