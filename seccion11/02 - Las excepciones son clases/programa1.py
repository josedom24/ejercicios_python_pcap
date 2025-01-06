try:
    i = int("¡Hola!")
except Exception as e:
    print(e)            # Imprime el mensaje de error
    print(e.__str__())  # Imprime la representación de la excepción
