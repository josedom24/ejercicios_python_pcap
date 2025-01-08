# Abre el archivo tzop.txt en modo lectura con codificación UTF-8
stream = open("text.txt", "rt", encoding="utf-8")

# Lee el contenido del archivo
content = stream.read()

# Imprime el contenido del archivo
print(content)

# Cuenta y muestra el número total de caracteres leídos
character_count = len(content)
print("Número total de caracteres leídos:", character_count)

# Cierra el stream
stream.close()
