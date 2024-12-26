# Usamos el método con literales cadenas
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())

# Usamos el método con una variable cadena
# La cadena no cambia, se devuelve una nueva cadena
cadena = "python"
print(cadena.capitalize())
print(cadena)

# Si queremos cambiar la cadena
cadena = cadena.capitalize()
print(cadena)