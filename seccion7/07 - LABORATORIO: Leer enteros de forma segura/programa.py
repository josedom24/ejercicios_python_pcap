def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            numero = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = numero >= min and numero <= max
        if not ok:
            print("Error: el valor no está dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return numero


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)