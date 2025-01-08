from os import strerror

try:
    counter = 0  # Inicializa el contador de caracteres
    stream = open('text.txt', "rt")  # Abre el archivo en modo lectura
    char = stream.read(1)  # Lee el primer carácter

    while char != '':  # Continúa hasta que no haya más caracteres
        print(char, end='')  # Imprime el carácter sin saltar a nueva línea
        counter += 1  # Incrementa el contador
        char = stream.read(1)  # Lee el siguiente carácter

    stream.close()  # Cierra el stream
    print("\n\nCaracteres en el archivo:", counter)  # Imprime el total de caracteres

except IOError as e:  # Manejo de excepciones
    print("Se produjo un error de E/S:", strerror(e.errno))

