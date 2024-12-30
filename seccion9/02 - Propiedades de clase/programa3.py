class ClaseEjemplo:
    varia = 1  # Variable de clase

    def __init__(self, val):
        ClaseEjemplo.varia = val  # Modificación de la variable de clase

# Imprime el diccionario de atributos de la clase antes de crear una instancia
print(ClaseEjemplo.__dict__)

# Crea una instancia de la clase
objeto = ClaseEjemplo(2)

# Imprime el diccionario de atributos de la clase después de crear una instancia
print(ClaseEjemplo.__dict__)

# Imprime el diccionario de atributos del objeto
print(objeto.__dict__)
