def mysplit(cadena):
    # Si la cadena está vacía o contiene solo espacios, devolver una lista vacía
    if cadena.strip() == "":
        return []
    
    # Dividir la cadena en palabras usando los espacios en blanco como delimitadores
    palabras = []
    letra_actual = ""
    for caracter in cadena:
        if caracter.isspace():
            if letra_actual:  # Si hay una palabra en construcción
                palabras.append(letra_actual)
                letra_actual = ""
        else:
            letra_actual += caracter
    # Agregar la última palabra si hay alguna
    if letra_actual:
        palabras.append(letra_actual)
    
    return palabras

print(mysplit("Ser o no ser, esta es una pregunta"))
print(mysplit("Ser o no ser, esta es una pregunta."))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

