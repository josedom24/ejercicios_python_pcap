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
            if char.isalpha():
                contadores[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    # Nota: hemos utilizado una lambda para acceder a los elementos del directorio y se ha establecido reverse a True para obtener un orden válido.
    for char in sorted(contadores.keys(), key=lambda x: contadores[x], reverse=True):
        c = contadores[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    