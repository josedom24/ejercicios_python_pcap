from os import strerror

try:
    character_counter = 0  # Inicializa el contador de caracteres
    line_counter = 0  # Inicializa el contador de líneas

    # Itera directamente sobre el objeto de archivo
    for line in open('text.txt', 'rt'):
        line_counter += 1  # Incrementa el contador de líneas
        for char in line:  # Itera sobre cada carácter en la línea
            print(char, end='')  # Imprime el carácter sin saltar a nueva línea
            character_counter += 1  # Incrementa el contador de caracteres

    # Cierre automático del archivo cuando se alcanza el final
    print("\n\nCaracteres en el archivo:", character_counter)  # Imprime el total de caracteres
    print("Líneas en el archivo:", line_counter)  # Imprime el total de líneas

except IOError as e:  # Manejo de excepciones
    print("Se produjo un error de E/S:", strerror(e.errno))
