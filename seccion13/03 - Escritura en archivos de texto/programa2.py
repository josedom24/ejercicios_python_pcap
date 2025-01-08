from os import strerror

try:
    # Abre el archivo en modo de escritura
    file = open('newtext.txt', 'wt')  # Crea o sobrescribe el archivo
    for i in range(10):
        file.write("línea #" + str(i + 1) + "\n")  # Escribe la línea completa
    file.close()  # Cierra el archivo
except IOError as e:  # Manejo de excepciones
    print("Se produjo un error de E/S:", strerror(e.errno))
