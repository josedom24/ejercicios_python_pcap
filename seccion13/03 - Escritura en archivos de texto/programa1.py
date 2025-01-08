from os import strerror

try:
    # Abre el archivo en modo de escritura
    file = open('newtext.txt', 'wt')  # Crea un nuevo archivo o lo sobrescribe
    for i in range(10):
        s = "línea #" + str(i + 1) + "\n"  # Crea la cadena para cada línea
        for char in s:
            file.write(char)  # Escribe carácter por carácter
    file.close()  # Cierra el archivo
except IOError as e:  # Manejo de excepciones
    print("Se produjo un error de E/S:", strerror(e.errno))
