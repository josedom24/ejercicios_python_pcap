cadena = 'x'
try:
    while True:
        cadena = cadena + cadena
        print(len(cadena))
except MemoryError:
    print('¡Esto no es gracioso!')