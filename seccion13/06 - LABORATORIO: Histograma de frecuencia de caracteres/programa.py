from os import strerror

# Inicializa 26 contadores para cada letra latina.
contadores = {}
for ch in range(ord('a'), ord('z') + 1):
    contadores[chr(ch)] = 0
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                contadores[char.lower()] += 1
    file.close()
    # Imprimamos los contadores.
    for char in contadores.keys():
        c = contadores[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))