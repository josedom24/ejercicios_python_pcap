from os import strerror

try:
    character_counter = 0  # Inicializa el contador de caracteres
    line_counter = 0  # Inicializa el contador de líneas
    stream = open('text.txt', 'rt')  # Abre el archivo en modo lectura
    line = stream.readline()  # Lee la primera línea

    while line != '':  # Continúa hasta que no haya más líneas
        line_counter += 1  # Incrementa el contador de líneas
        for char in line:  # Itera sobre cada carácter en la línea
            print(char, end='')  # Imprime el carácter sin saltar a nueva línea
            character_counter += 1  # Incrementa el contador de caracteres
        line = stream.readline()  # Lee la siguiente línea

    stream.close()  # Cierra el stream
    print("\n\nCaracteres en el archivo:", character_counter)  # Imprime el total de caracteres
    print("Líneas en el archivo:", line_counter)  # Imprime el total de líneas

except IOError as e:  # Manejo de excepciones
    print("Se produjo un error de E/S:", strerror(e.errno))
